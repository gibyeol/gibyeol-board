/* POST /api/feedback — the "anything wrong or missing?" form at the bottom of every page.
   Owner 2026-11-28: (가) store on the site [7eb4ec94#4932], repository nadri-feedback (question window).
   Flow (Cloudflare docs read 2026-11-28, copies in wondu-archive raw-from-scratchpad/feedback-docs-2026-11-28):
   1. check the Turnstile token with Siteverify (server-side validation is mandatory);
   2. write one JSON file to the private repository with GitHub "Create or update file contents"
      (fine-grained token, repository permission Contents: write, only this repository).
   Secrets (Cloudflare Pages > Settings > Variables and Secrets, Encrypt): TURNSTILE_SECRET, FEEDBACK_GITHUB_TOKEN.
   Nothing about the visitor is stored except what they typed, the page and its language. No IP address is sent or kept. */
const REPO = "gibyeol/nadri-feedback";
const KINDS = ["wrong", "missing", "other"];
const LANGS = ["en", "ko", "ja", "zh-tw"];
const MAX = 2000;

function reply(status, data) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });
}

function base64(text) {
  const bytes = new TextEncoder().encode(text);
  let bin = "";
  for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  return btoa(bin);
}

export async function onRequestPost({ request, env }) {
  if (!env.TURNSTILE_SECRET || !env.FEEDBACK_GITHUB_TOKEN) return reply(503, { ok: false, error: "not_configured" });
  const host = new URL(request.url).hostname;
  const origin = request.headers.get("origin");
  let originHost = "";
  try {
    originHost = origin ? new URL(origin).hostname : host;
  } catch (e) {
    originHost = "";
  }
  if (originHost !== host) return reply(403, { ok: false, error: "origin" });
  if (Number(request.headers.get("content-length") || 0) > 16384) return reply(413, { ok: false, error: "too_large" });

  let d;
  try {
    d = await request.json();
  } catch (e) {
    return reply(400, { ok: false, error: "bad_json" });
  }
  if (!d || typeof d !== "object") return reply(400, { ok: false, error: "bad_json" });
  const kind = String(d.kind || "");
  const lang = String(d.lang || "");
  const page = String(d.page || "");
  const body = String(d.body || "").trim();
  const token = String(d.token || "");
  if (!KINDS.includes(kind) || !LANGS.includes(lang) || !/^\/[a-z0-9\-\/]{0,200}$/.test(page) || !body || body.length > MAX || !token) {
    return reply(400, { ok: false, error: "invalid" });
  }

  let v = { success: false };
  try {
    const r = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ secret: env.TURNSTILE_SECRET, response: token }),
    });
    v = await r.json();
  } catch (e) {
    return reply(502, { ok: false, error: "verify_unreachable" });
  }
  if (!v.success || (v.hostname && v.hostname !== host)) return reply(403, { ok: false, error: "verify" });

  const now = new Date();
  const stamp = now.toISOString();
  const id = stamp.replace(/[:.]/g, "-") + "-" + crypto.randomUUID().slice(0, 8);
  const record = { received_at: stamp, page, lang, kind, body, status: "new" };
  const path = `feedback/${stamp.slice(0, 10)}/${id}.json`;
  const put = () =>
    fetch(`https://api.github.com/repos/${REPO}/contents/${path}`, {
      method: "PUT",
      headers: {
        authorization: `Bearer ${env.FEEDBACK_GITHUB_TOKEN}`,
        accept: "application/vnd.github+json",
        "content-type": "application/json",
        "user-agent": "nadri-feedback-form",
      },
      body: JSON.stringify({ message: `feedback: ${kind} ${page}`, content: base64(JSON.stringify(record, null, 2) + "\n") }),
    });
  try {
    let r = await put();
    // two files written at the same moment can conflict (GitHub docs: run these requests serially): retry once
    if (r.status === 409) {
      await new Promise((ok) => setTimeout(ok, 800));
      r = await put();
    }
    if (!r.ok) return reply(502, { ok: false, error: "store" });
  } catch (e) {
    return reply(502, { ok: false, error: "store_unreachable" });
  }
  return reply(200, { ok: true });
}
