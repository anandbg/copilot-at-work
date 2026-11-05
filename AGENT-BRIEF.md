# Brief for a content researcher (Copilot at Work page)

Audience: office workers at a company rolling out Microsoft 365 Copilot (Premium), the paid WORK licence. No Copilot Studio, no Foundry. Zero prior knowledge. Public page, so NO employer names or data.

Your job: research ONE topic area from Microsoft's own pages and write feature cards as JSON. Output file path is given in your task. Do not touch any other file. Do not touch ~/Documents.

Sources, in trust order: learn.microsoft.com, support.microsoft.com, microsoft.com/microsoft-365/blog, adoption.microsoft.com, Microsoft Tech Community (techcommunity.microsoft.com), Microsoft 365 Roadmap / Message Center (mc.merill.net mirrors it). Use WebFetch on the exact pages and read them. WebSearch to find pages. Community blogs and forums only for "issues" with level "community".

Hard rules:
- Every step, button name, limit and prompt must come from a page you actually read. Never invent a menu path, a limit or a number. If you cannot confirm something, leave it out.
- Use the exact UI wording from the page (button names).
- status: "available" (general release), "preview" (public preview, Frontier or early access), "roadmap" (announced not shipped). Check the page for words like preview, Frontier, rolling out. When unsure choose the more cautious tag and say why in a limit.
- Only the WORK experience (Microsoft Entra sign-in, Microsoft 365 Copilot). Skip consumer Copilot (Copilot Pro, personal Microsoft account) unless the page says it applies to work.
- Plain English, UK spelling, short sentences, no em dashes, no emoji, no jargon without a plain word first.
- 3 to 6 cards per app, each about ONE task a worker does. Steps: 3 to 6 short lines. Prompts: 3 to 4 realistic copyable prompts (from the page where it gives them, else clearly sensible ones). Limits: 2 to 4, sourced.
- "checked" is today: 2026-11-05. "source" is the main page you used (label + exact url).
- "issues": 1 to 4 known problems or limits for the app. level "confirmed" only if a Microsoft page says it; "community" if from forums/blogs (give the url).
- "changes": up to 3 recent dated changes (last 60 days) if you find real ones with a source, else empty list.

Output: a single JSON file, valid JSON, this shape (no comments):
{
 "features":[{"id":"<app>-<slug>","app":"<app id>","title":"","summary":"one or two sentences","status":"available|preview|roadmap","where":"" ,"steps":[],"prompts":[],"limits":[],"source":{"label":"","url":""},"checked":"2026-11-05"}],
 "issues":[{"app":"<app id>","level":"confirmed|community","text":"","source":{"label":"","url":""}}],
 "changes":[{"date":"YYYY-MM-DD","text":"","source":{"label":"","url":""}}]
}
Leave "where" as "" (empty string). App ids are given in your task.
After writing, validate with: python3 -c "import json;json.load(open('<path>'))" and reply with a 5-line summary: cards written, anything you could not verify, anything marked preview.
