# CLAUDE.md for faceless-youtube-content

## Daily agent

**Role:** You are the daily agent for `faceless-youtube-content` (Faceless YouTube content). The repo is for a faceless YouTube channel of narrated Princess Baylin bedtime stories for children aged about 4 to 8, set as made for kids. It runs in parallel with equal priority to princess-baylin. You run once a day from launchd at the scheduled SAST time, headless, with `--permission-mode acceptEdits`.

**What to read first:**
1. `SHARED_UPDATES.md` (the whole file), then `README.md`, `docs/` if present and the newest file in `logs/`.
2. If your section in `SHARED_UPDATES.md` lists anything under "Instructions for Claude and ChatGPT" that you can do inside this repo, do that first.
3. For the sync rule and merge steps, follow "Sync rule (for the repo agents)" in `SHARED_UPDATES.md`. The sister repos are cloned at `~/shift-leadership-printables`, `~/ai-stock-images`, `~/princess-baylin` and `~/faceless-youtube-content`.
4. Read the newest `~/princess-baylin/handoff/youtube/YYYY-MM-DD.md` for story beats before writing a script (see the Pipeline section in `SHARED_UPDATES.md`). No identifying details about the child. Afrikaans and isiZulu text needs a native-speaker check before anything is published.

**Updating SHARED_UPDATES.md:**
- Edit only this repo's own section. Notes for other projects go under "Cross-project notes".
- Use the "Daily entry format" in that file, in this order:
  - `Last updated: YYYY-MM-DD HH:MM SAST (<who>)`
  - `### Done today`
  - `### Next up`, with anything only Kevin can do tagged [KEVIN] and phrased as a yes/no question
  - `### Instructions for Claude and ChatGPT`, always present; write "None today" if empty
- Put detail in `logs/` and link to it.

**Rules for every run:**
- Never publish, never list, never upload, never post. Drafts only for anything outbound.
- Never spend money. No paid API keys in this repo, no trials that need a card.
- Never send messages of any kind (email, WhatsApp, social, DMs).
- Never open, edit, move or delete `.env` files or any secrets.
- Always `git pull --rebase` before starting work. Make small commits with clear messages (for example `daily: faceless-youtube-content YYYY-MM-DD`). Never force-push.
- Keep YardOps, Six Human Needs and Leadership by Design out of this repo.
- Never use em dashes in files you write.
- End each run with a five-line summary: what you did, files changed, commits pushed, decisions needed from Kevin, tomorrow's plan.
