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

## Decisions (Kevin, 2026-11-14 SAST)

Kevin approved the 100-video plan and its eleven decisions, then said "You decide on everything". The full list is in `~/princess-baylin/CLAUDE.md` and `~/princess-baylin/docs/series-plan-100.md`. What changes in this repo:

1. The hold on Episode 7 onward is lifted. New episode scripts are written by Claude, two a week, in slate order, from `~/princess-baylin/docs/100-video-slate.md` (procedure: `docs/weekly-script-run.md`). The daily agent does not write new episode scripts. It works on production packs, shot boards, critiques and the status file. `scripts/README.md` lists every script and its status.
2. Episodes 4, 5 and 6 are approved with the critique fixes applied. Episodes 7 and 8 are written and approved for art and the English render.
3. Every new script follows `docs/channel-style-guide.md`: a 30-second hook, 13 beats with the close split in two, one calm cue with a child pause, a Calm Minute Short, and Bonayo's closing line matched to the lesson.
4. A story must not put Baylin through the same situation and outcome as an earlier episode. In particular, she does not open by racing ahead and close by slowing down again.
5. Check every script with `python3 scripts/check_pace.py <file>` before committing it. Every beat reads at 85 to 120 words a minute.
6. Placeholder names are kept unless the original story says otherwise. English first; Afrikaans and isiZulu wait for a named native-speaker reviewer.

**Delegation.** Claude decides the remaining story, script, slate and production questions and records each one in `logs/`. A script Claude marks approved is cleared for art and the English render. The rules for every run above are unchanged: an agent never publishes, uploads, posts, sends messages or spends money. Kevin watches each finished video before it is made public.

The channel is live at https://www.youtube.com/@PrincessBaylinDiaries. Episode 1 is live and public at https://www.youtube.com/watch?v=BrF_v5ACTxo. Do not write any email address into this repo.
