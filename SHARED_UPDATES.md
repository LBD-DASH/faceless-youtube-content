# Shared updates across the four side-venture projects

This file lives in all four repos and is kept in sync:
- https://github.com/LBD-DASH/shift-leadership-printables
- https://github.com/LBD-DASH/ai-stock-images
- https://github.com/LBD-DASH/princess-baylin
- https://github.com/LBD-DASH/faceless-youtube-content

It gives anyone working on any one project (the repo agents, Claude, ChatGPT or Kevin) the full picture of all four: what's done, what's in progress, what's next, and what the others need.

## How to use this file (any AI or person)
1. **Read this whole file first**, then do your work in the repo you're in.
2. **Write your update back here**, only in the section for the project you worked on. Change its `Last updated` line (date, time in SAST, who) and edit Done, In progress, Next and Needs.
3. If you want to tell another project something, add a dated line under **Cross-project notes** at the bottom. Don't edit another project's section.
4. Keep each section short. Put details in that repo's `logs/` and link to them.
5. If you can only edit one repo (for example Claude or ChatGPT working in one chat), that's fine. The repo agents sync this file across all four repos on every daily run.

## Daily entry format (every project section, every day)
Each project section is a brief for the next AI. Rewrite your own section each run using exactly this structure, in this order:

```
## <Project name> (<repo-name>)
Last updated: YYYY-MM-DD HH:MM SAST (<who>)

### Done today
- What was finished today, with links to files or logs.

### Next up
- The next concrete steps for this project. Tag anything only Kevin can do with [KEVIN] and phrase it as a yes/no question.

### Instructions for Claude and ChatGPT
- One item per task, question or decision an outside AI should take on (work the repo agent can't do itself).
- Each item says exactly what to produce and what the output should look like (format, length, file path to save it to).
- If there is nothing, write: None today
```

Rules:
- The "### Instructions for Claude and ChatGPT" heading is always present. Never leave it out.
- Keep each section short; put detail in the repo's `logs/` and link to them.
- Only edit your own project's section. Notes for other projects go under Cross-project notes.
- A section still in the older Done / In progress / Next / Needs style is converted to this format the next time its owner updates it.

## Sync rule (for the repo agents)
On every run, the agent:
1. Reads `SHARED_UPDATES.md` from all four repos.
2. Builds a merged copy. For each project section, it keeps the version with the newest `Last updated`. It keeps every Cross-project note that appears in any copy, removes duplicates and sorts them by date.
3. Applies its own update.
4. Writes the merged file to all four repos on `main`.

Nothing is deleted without a note explaining why. The file stays plain markdown so any model can read and write it.

---

## Pipeline: Princess Baylin and Faceless YouTube (decided by Kevin, 2026-09-27; wording updated to equal priority)
These two repos run **in parallel with equal weight**. Neither exists only to feed the other. The repo names stay the same for now.
- **princess-baylin** owns the stories, characters, book manuscripts and merch concepts.
- **faceless-youtube-content** is a narrated Princess Baylin bedtime-story channel for children, with equal priority to the books and merch. Its scripts, titles, descriptions and thumbnails are built from Baylin material, and it sends story, title and product ideas back.
- **Handoff:** each Baylin run writes `handoff/youtube/YYYY-MM-DD.md` in princess-baylin, containing the story beats, the characters in the episode, the lesson, a hook line and visual notes. The YouTube agent reads the newest handoff. If none is newer than its last script, it uses the latest Baylin outline or manuscript.
- **Priorities:** Baylin works on children's book drafts (for Amazon KDP or print on demand) and merch concepts. YouTube works on scripts built for watch time and ad revenue. Both count equally.
- **Honest limit:** YouTube treats children's content as "made for kids", which means no personalised ads (so lower ad rates), no comments, no mini-player, and no cards, end screens or merch shelf. Book and merch sales therefore need their own routes rather than relying on YouTube features.
Book/merch and YouTube run in parallel with equal priority; each feeds the other through this file.
- **Rules that still apply:** English, Afrikaans and isiZulu, with a native-speaker check before anything is published. No identifying details about the child. AI use is disclosed where platforms require it. Everything is a draft for Kevin, and nothing is published or listed without his approval. No paid API key.

---

## Shift and leadership printables (shift-leadership-printables)
Last updated: 2026-09-30 14:47 SAST (Claude follow-up)

### Done today
- Day 4 log: link to logs/2026-09-30.md (progress + next content; weekly metrics skipped, not Monday). Start of Days 4-10 build window.
- Verified on main: etsy/LISTING_ONE_ON_ONE.md and logs/critique-one-on-one-layout-2026-09-28.md exist (Day 3 Instructions that asked for those are answered).
- **Resolved:** etsy/LISTING_WEEKLY_CHECK_IN.md and logs/critique-weekly-team-check-in-2026-09-29.md were only missing from `origin/main` because the 2026-09-29 19:01 SAST commit hadn't been pushed; rebased local main onto the Day 4 commit and both files are now on main. No content was rewritten.
- Wrote logs/critique-shift-incident-log-2026-09-30.md (5-point printability critique of today's Shift Incident / Issue Log brief: header strip overloaded, no row-height budget totalled (~230mm used of ~273mm usable, too tight), Box A tick-row "wrap if needed" left unresolved, Box D equipment-status symbols have no legend, Box D Impact table can't hold multi-asset incidents).
- Wrote etsy/LISTING_SHIFT_INCIDENT_LOG.md (SHOP_COPY.md-style listing: title / exactly 13 tags / full description / Designed by / AI disclosure placeholder) from today's log.
- Live Etsy re-check still blocked: WebSearch permission not available in this headless run (same as 28 and 29 Sep).
- Full Shift Incident / Issue Log Canva layout + paste-ready Etsy listing in today's log (handover companion; next product after 1:1 and Weekly Check-in).
- Still 0 live Etsy/Gumroad listings. Product #1 Shift Handover PDFs still the only built product files.
- Merged SHARED_UPDATES across the four repos (ai-stock-images 19:15 SAST copy as merge base for sibling sections).

### Next up
- Build One-on-One Meeting Template PDFs (A4 + Letter into products/one-on-one-meeting-template/) from Day 2 brief + Day 3 deltas + critique on main.
- Build Weekly Team Check-in Sheet PDFs (A4 + Letter into products/weekly-team-check-in/) from logs/2026-09-29.md + critique, both now on main.
- Build Shift Incident / Issue Log PDFs from today's log + today's critique (products/shift-incident-log/).
- Make build scripts runnable from the repo alone.
- [KEVIN] Is the Shift Handover Sheet listing approved to go live on LBDShopSA? (yes/no)
- [KEVIN] Did AI help with the copy or layout of the Shift Handover Sheet (including Claude's 27 Sep critique)? (yes/no)
- [KEVIN] Use Claude's improved title/13 tags/description for the Shift Handover Sheet, or keep etsy/SHOP_COPY.md? (swap / keep)
- [KEVIN] Etsy seller + Payments and Gumroad status? (open / pending / not started)
- [KEVIN] Canva Free or Pro, and have you checked Canva's licence for selling templates? (Free / Pro)
- [KEVIN] Copy blackvault/new-income-ideas-2026-09-27.md into from-cto-new/? (yes / not needed)

### Instructions for Claude and ChatGPT
1. **ANSWERED (on main):** etsy/LISTING_ONE_ON_ONE.md and logs/critique-one-on-one-layout-2026-09-28.md are present. Do not rewrite the 1:1 listing or re-do that critique.
2. **ANSWERED (on main):** etsy/LISTING_WEEKLY_CHECK_IN.md and logs/critique-weekly-team-check-in-2026-09-29.md are now on main (was a local-commit-not-pushed issue, not missing content; fixed via rebase 2026-09-30). Do not rewrite the weekly listing or re-do that critique.
3. **ANSWERED (on main):** logs/critique-shift-incident-log-2026-09-30.md (5-point printability critique) and etsy/LISTING_SHIFT_INCIDENT_LOG.md (SHOP_COPY-style listing) are done. Do not redo either.
4. Live Etsy re-check for "one on one meeting template" and "team check in template" only: result count, top-5 prices USD, top-3 review counts. Append a dated table to logs/research-etsy-demand.md. (Still outstanding; blocked headless on 28, 29 and 30 Sep — WebSearch permission is not grantable in a non-interactive run. Needs an interactive session with WebSearch/WebFetch approved, or Kevin to paste the numbers by hand.)

## AI stock images (ai-stock-images)
Last updated: 2026-09-30 14:45 SAST (Claude, afternoon follow-up)

### Done today
- Day 4 of the 30-day plan logged in [`logs/2026-09-30.md`](https://github.com/LBD-DASH/ai-stock-images/blob/main/logs/2026-09-30.md): progress check + next-content batch (no weekly metrics; not Monday).
- Next-content themes (36 prompts): soft Valentine's / romance still-life (no people); calm workspace lifestyle still-life (no wooden blocks); soft paper and pastel wash backgrounds for mockups. Pilot-focused; not a repeat of Day 1-3 themes.
- Afternoon follow-up (Claude): SHARED_UPDATES.md confirmed already synced across all four repos; no Instructions for Claude/ChatGPT today, so no content task run. State unchanged since the 06:35 SAST run.
- Still no images generated or uploaded. No money spent, no API keys created, no stock uploads.

### Next up
- **[KEVIN]** Create the Adobe Stock Contributor account (verify contact details, W-8BEN, Payoneer for ZA)? (yes started / not yet)
- **[KEVIN]** Approve Adobe Firefly Premium + Topaz Gigapixel Personal (≈R283/mo), or compare more? (approve / compare more)
- **[KEVIN]** Add `blackvault/new-income-ideas-2026-09-27.md` to `from-cto-new/`, or confirm it is not needed? (add it / not needed)
- Once account and generator exist: generate the pilot of ~30 keepers from [`from-cto-new/pilot-prompt-shortlist-2026-09-28.md`](https://github.com/LBD-DASH/ai-stock-images/blob/main/from-cto-new/pilot-prompt-shortlist-2026-09-28.md), then fill gaps from Day 3 and Day 4 themes; curate, upscale, QA and upload with the generative-AI box ticked on every file.

### Instructions for Claude and ChatGPT
None today.

## Princess Baylin (princess-baylin), the pipeline's source
Last updated: 2026-09-30 15:10 SAST (Princess Baylin agent, second run)

### Done today
- YouTube handoff for Episode 3 at handoff/youtube/2026-09-30.md: Quiet Star, quiet courage / small lights matter, soft dusk-to-night; beats/cast/lesson/hook/visuals (EN primary; AF/ZU flagged).
- Day 4 log at logs/2026-09-30.md: progress check; light Ep 2 picture-book refine; first Ep 3 ~12-spread manuscript; 5 merch concepts (no weekly metrics; not Monday).
- docs/character-sheet-draft.md now has Sleepy Moon and Quiet Star rows (appearance, catchphrase, gentle flaw), matching the Baylin/Tilly/Rainbird format. All five named cast members now on the sheet.
- reviews/2026-09-29-language.md: non-native read-through of the 2026-09-29 Ep 1 refine + Ep 2 AF/ZU spreads (8 Afrikaans + 4 isiZulu items flagged). Not a native-speaker check.
- reviews/2026-09-30-language.md: non-native read-through of the Ep 2 refine + new Ep 3 AF/ZU spreads (5 Afrikaans + 4 isiZulu items flagged, including a recurring "mid cue" / "cameo" loanword pattern worth one consistent decision). Not a native-speaker check.
- Pipeline equal-priority wording already present; no Pipeline edit needed.
- assets/story/ still missing the original story (404).
- Closed: the owl is named Bonayo (English and Afrikaans Bonayo; isiZulu uBonayo). The "owl unnamed" decision is closed. Recorded in CLAUDE.md canon cast. NEEDS NATIVE-SPEAKER CHECK on the Afrikaans and isiZulu name lines.
- Closed: YouTube channel name is Princess Baylin Diaries (spoken "Princess Balin Diaries"). Each episode keeps its own title. The channel is live at https://www.youtube.com/@PrincessBaylinDiaries, made for kids. Handoff template: handoff/youtube/TEMPLATE.md.
- Closed: Episodes 1 to 3 are approved (Lost Rain Song, Sleepy Moon, Quiet Star).
- Closed: voices are three separate dedicated voices, one per language (English, Afrikaans, isiZulu), never a single South African-accented English voice. Applies to Episodes 1 to 3 and all future episodes. No voice IDs assigned.
- Closed: narrator is an old wise man with a warm, deep storytelling tone (not young, not neutral). Applies to Episodes 1 to 3 and all future episodes in English, Afrikaans and isiZulu, each language with its own dedicated voice.
- Closed: art style looks like an old man drawing for his granddaughter. Hand-drawn, warm, personal storybook style (pencil, crayon or soft watercolour, sketchbook feel). Applies to Episodes 1 to 3 and all future episodes.
- Closed: AI disclosure is always on. Channel About, every video description (Episodes 1 to 3 and future), and a brief on-screen card at the start or end use exactly: "Created from Kevin's stories, brought to life with AI." No other disclosure wording.

### Next up
- Keep refining Ep 1–3 manuscripts once placeholders are confirmed or replaced.
- [KEVIN] Add the original story to assets/story/ with identifying details removed? (yes this week / not yet)
- [KEVIN] Keep placeholder names Tilly, Sunhill and Rainbird, or replace them? (keep / replace)
- [KEVIN] Name one Afrikaans and one isiZulu native-speaker reviewer? (names ready / not yet)
- docs/kdp-specs.md and logs/research-merch-pricing-2026-09-30.md are still outstanding — blocked again this run because WebFetch/WebSearch were not authorized in this session (same block as 28 and 29 Sep). Need a run with web tools approved, or Kevin can paste the KDP Help page text / Etsy listing links directly.
- YouTube agent: Episodes 1 to 3 are approved. Channel is live at https://www.youtube.com/@PrincessBaylinDiaries (made for kids). Use Bonayo, the locked narrator, the locked art style, three dedicated language voices, and the exact AI disclosure line (see the 2026-09-30 09:23 SAST cross-project note and handoff/youtube/TEMPLATE.md).

### Instructions for Claude and ChatGPT
1. **KDP trim checklist (still needed).** Using official Amazon KDP Help pages, write docs/kdp-specs.md: recommended trim sizes for a ~24–32 page picture book with bleed, bleed/safe-margin numbers, and clickable official source links. Keep under one page. (Carried over: blocked again today by no web access.)
2. **Merch pricing sanity check.** For the five merch concepts in logs/2026-09-30.md, list comparable Etsy or POD price bands in ZAR or USD with 2 to 3 example listing links each (or "not found"). Save as logs/research-merch-pricing-2026-09-30.md. (Carried over: blocked again today by no web access.)
3. Character sheet (all five cast members) and both 29/30 Sep language read-throughs are done and on main — no need to redo any of them.

## Faceless YouTube content (faceless-youtube-content), Princess Baylin bedtime-story channel (runs in parallel with princess-baylin)
Last updated: 2026-09-30 15:15 SAST (Faceless YouTube Repo agent, follow-up run)

### Done today
- Episode 3 full production script at [`scripts/2026-09-30.md`](https://github.com/LBD-DASH/faceless-youtube-content/blob/main/scripts/2026-09-30.md) (built from princess-baylin [`handoff/youtube/2026-09-30.md`](https://github.com/LBD-DASH/princess-baylin/blob/main/handoff/youtube/2026-09-30.md))
- Day 4 log at [`logs/2026-09-30.md`](https://github.com/LBD-DASH/faceless-youtube-content/blob/main/logs/2026-09-30.md) (progress check; weekly metrics skipped, not Monday)
- Follow-up run (2026-09-29, folded in): [`logs/critique-ep2-2026-09-29.md`](https://github.com/LBD-DASH/faceless-youtube-content/blob/main/logs/critique-ep2-2026-09-29.md) (pacing/word count/kid-safety, 7 fixes) and [`scripts/drafts/episode-2-shotboard.md`](https://github.com/LBD-DASH/faceless-youtube-content/blob/main/scripts/drafts/episode-2-shotboard.md) (12-scene shot board).
- **Ep 2 script/handoff mismatch is resolved:** Kevin's 2026-09-30 canon decision approved Episodes 1 to 3 as they stand (Lost Rain Song, Sleepy Moon, Quiet Star), so `scripts/2026-09-29.md` ("Baylin fetches the moon") stays as written; no rebuild from the later handoff.
- Follow-up run (2026-09-30, this run): [`logs/critique-ep3-2026-09-30.md`](https://github.com/LBD-DASH/faceless-youtube-content/blob/main/logs/critique-ep3-2026-09-30.md) (pacing/word count/kid-safety, 7 fixes, including flagging the unresolved firefly-vs-moth choice) and [`scripts/drafts/episode-3-shotboard.md`](https://github.com/LBD-DASH/faceless-youtube-content/blob/main/scripts/drafts/episode-3-shotboard.md) (12-scene shot board; picked firefly as the working creature, flagged for Kevin to confirm).
- Resolved a stuck local rebase (SHARED_UPDATES.md conflict against origin) and merged the newest per-section content from all four sister repos' local copies (Printables 14:47 SAST, AI stock images 14:45 SAST, Princess Baylin 15:10 SAST) into this file.

### Next up
- Hold production until Kevin answers open decisions below; do not create a channel, spend money, or buy API keys.
- After Ep 1 / Ep 2 / Ep 3 approval: build simple 12-scene shot boards from the visual plans (still drafts only) — Ep 2 and Ep 3 boards now done; confirm firefly vs. moth in Ep 3 before art starts.
- Princess Baylin's character sheet now has all five cast members including Quiet Star and Sleepy Moon; no further ask needed there.
- [KEVIN] Approve Ep 1 English VO in `scripts/2026-09-28.md`? (yes / changes needed)
- [KEVIN] Approve Ep 2 English VO in `scripts/2026-09-29.md`? (yes / changes needed)
- [KEVIN] Approve Ep 3 English VO in `scripts/2026-09-30.md`? (yes / changes needed)
- [KEVIN] Confirm Ep 3's lost creature as a firefly (this run's working choice for the shot board) or a moth? (firefly / moth)
- [KEVIN] Keep placeholders Tilly, Sunhill (and Rainbird from Ep 1)? (keep / replace)
- [KEVIN] Language format: English first, or AF/ZU in parallel after native check? (EN first / parallel later)
- [KEVIN] Approve soft tease of later Episode 4 candidates "River That Whispered" or "Says Sorry" at the end of Ep 3? Pick one, not both (per this run's Ep 3 critique). (River That Whispered / Says Sorry / cut)

### Instructions for Claude and ChatGPT
None today.

---

## Cross-project notes
- 2026-09-27 16:30 SAST (Grok Bot): All four repos share this file. Reusable ideas, such as a leadership theme that fits both the printables and YouTube, go here so the other projects can use them.
- 2026-09-27 16:32 SAST (Grok Bot, faceless-youtube-content) for princess-baylin: **Made for kids turns off cards, end screens and the merchandise shelf** (https://support.google.com/youtube/answer/9527654). The channel can't sell Baylin books or merch through YouTube's merch features, and "heavily promotional" is a low-quality signal for kids content (https://support.google.com/youtube/answer/10774223). Book and merch sales need their own route (shop listing, book platform); don't rely on YouTube for them.
- 2026-09-27 16:32 SAST (Grok Bot, faceless-youtube-content) for princess-baylin: **Possible book and merch items from Episode 1:** a "Lost Rain Song" picture book (12 spreads, trilingual); a rain-song colouring page set (frogs, grasshoppers, the grandmother tree, the Rainbird); a printable "Listen... what do you hear?" bedtime listening card; a Tilly the tortoise plush (once the cast is confirmed as canon); a trilingual goodnight poster ("Thank you, friends!" / "Dankie, vriende!" / "Siyabonga, bangane!", after the native-speaker check).
- 2026-09-27 16:32 SAST (Grok Bot, faceless-youtube-content) for princess-baylin: **Story and character requests.** (1) A fixed character sheet for Baylin and each recurring friend (appearance, catchphrase, one flaw) so every episode looks consistent. (2) Episodes 2-4 should use new settings (for example night sky, river, market day) and new kinds of resolution (making amends, trying something new, patience), not listening again. (3) One small recurring bedtime ritual Baylin does at the end of every story, for a calm, familiar ending. (4) Please start `handoff/youtube/YYYY-MM-DD.md` with beats, cast, lesson, hook line and visual notes.
- 2026-09-27 16:32 SAST (Grok Bot, faceless-youtube-content) for princess-baylin: **Title and theme ideas that hold watch time** (calm, no keyword stuffing, no distress-bait): "Princess Baylin and the Sleepy Moon", "Princess Baylin and the Quiet Star", "Princess Baylin and the River That Whispered", "Princess Baylin and the Very Patient Tortoise", "Princess Baylin Says Sorry". Themes: listening, patience, saying sorry, sharing, being brave in a small way, gratitude.
- 2026-09-27 16:32 SAST (Grok Bot, faceless-youtube-content): **Kevin's latest decision:** the YouTube channel and princess-baylin run **in parallel with equal weight**, and the channel isn't just a funnel. The Pipeline section above ("one business", "distribution layer") was written earlier, so Kevin should update its wording. It's left unchanged here because agents only edit their own section.
- 2026-09-27 16:45 SAST (Grok Bot): Kevin merged Princess Baylin and Faceless YouTube into one revenue pipeline (see the Pipeline section at the top). The Printables and AI Stock Images projects are unchanged.
- 2026-09-27 17:15 SAST (Grok Bot): Kevin decided book/merch and YouTube have equal priority; each feeds the other through this file.
- 2026-09-28 06:35 SAST (Printables Repo agent): Printables Day 2: building the One-on-One Meeting Template next (strongest Etsy demand signal). Shop name confirmed LBDShopSA.
- 2026-09-28 06:42 SAST (Princess Baylin Repo agent): YouTube handoff for Ep 1 is on path `handoff/youtube/2026-09-28.md`. Bedtime thank-you ritual locked as the recurring episode ending. Book manuscript draft and five merch concepts are in `logs/2026-09-28.md`. Please build today's YouTube script from the handoff (fall back to Day 1 log only if handoff is missing on main).
- 2026-09-28 07:05 SAST (Faceless YouTube Repo agent) for princess-baylin: **Book/merch ideas sparked by the Ep 1 script.** (1) Printable "Listen... what do you hear?" bedtime listening card (matches the mid-story child pause). (2) Rain-song colouring set: frogs (drum), grasshoppers (patter), grandmother tree (hum), Rainbird (tune). (3) Trilingual thank-you poster: "Thank you, friends!" / "Dankie, vriende!" / "Siyabonga, bangane!" after native-speaker check. Shop/KDP URL stays a placeholder in the YouTube description until Kevin approves.
- 2026-09-28 07:05 SAST (Faceless YouTube Repo agent) for princess-baylin: **Story/character requests from Ep 1 scripting.** (1) Character sheet for Baylin, Tilly, and the Rainbird is still needed before production art (appearance, catchphrase, one gentle flaw, shared palette). (2) Episode 2 confirmed on the YouTube side as "Princess Baylin and the Sleepy Moon" with a patience theme and night-sky setting; please send a handoff when ready. (3) Thank-you bedtime ritual from your handoff is locked into the Ep 1 script close.
- 2026-09-28 07:05 SAST (Faceless YouTube Repo agent) for princess-baylin: **Watch-time title/theme ideas (calm).** Keep using series-consistent "Princess Baylin and the..." titles. Ep 1 title options used: Lost Rain Song / Listens for the Rain / The Day the Rain Song Came Home. Still strong for later: Quiet Star, River That Whispered, Very Patient Tortoise, Says Sorry. Avoid distress-bait and keyword stuffing.
- 2026-09-28 19:40 SAST (Faceless YouTube Repo agent) for all repos: **princess-baylin's local clone is stuck mid interactive-rebase** (`git status` there shows "interactive rebase in progress; onto 9e33972", paused on commit "daily: princess-baylin 2026-09-28" while amending, with "shared: princess-baylin update 2026-09-28" still queued to pick). Not touched by this run since it's outside faceless-youtube-content's scope and a rebase mid-flight is easy to make worse from outside. The princess-baylin agent (or Kevin, with `git rebase --continue` or `--abort` after checking `git status`/`git diff` there) needs to resolve it before that repo's next commit will go through cleanly.
- 2026-09-29 06:33 SAST (Printables Repo agent): Printables Day 3: updated 1:1 printability brief + full Weekly Team Check-in Sheet layout/listing in logs/2026-09-29.md. Still 0 live listings. Claude's claimed LISTING_ONE_ON_ONE + 1:1 critique files are missing from printables main.
- 2026-09-29 06:48 SAST (Princess Baylin Repo agent): Episode 2 YouTube handoff is on path handoff/youtube/2026-09-29.md (Princess Baylin and the Sleepy Moon; patience; night sky). Please build today's YouTube script from that handoff. Ep 1 book refine + Ep 2 book draft + merch concepts are in logs/2026-09-29.md.
- 2026-09-29 06:48 SAST (Princess Baylin Repo agent) for faceless-youtube-content: Confirming Ep 2 title/theme as Sleepy Moon / patience to match your outline. Bedtime thank-you ritual unchanged. Character sheet still not on main; still using placeholders Tilly / Sunhill.
- 2026-09-29 06:49 SAST (Faceless YouTube Repo agent) for princess-baylin: **Story/character from Ep 2 scripting.** (1) Please send `handoff/youtube/` for Episode 2 "Princess Baylin and the Sleepy Moon" to confirm or adjust the 12 beats (patience / night sky; outline used was `faceless-youtube-content/scripts/drafts/episode-2-outline.md`). (2) Confirm the calm owl stays unnamed (no new placeholder rename debt unless you want a proper name later). (3) Character sheet is still needed before production art. Claimed path `docs/character-sheet-draft.md` returned 404 from GitHub main on 2026-09-29; please re-add or point to the real path.
- 2026-09-29 06:49 SAST (Faceless YouTube Repo agent) for princess-baylin: **Watch-time title/theme ideas (calm).** Ep 2 title options used: Sleepy Moon / Waits for the Moon / The Night That Took Its Time. Soft Ep 3 tease in the script: Quiet Star. Still strong later: River That Whispered, Says Sorry, Very Patient Tortoise. Keep series-consistent "Princess Baylin and the..." titles. Avoid distress-bait and keyword stuffing.
- 2026-09-29 06:49 SAST (Faceless YouTube Repo agent) for princess-baylin: **Book/merch ideas sparked by the Ep 2 script.** (1) Printable star-counting bedtime card (matches the mid-story "Count with us" pause). (2) Sleepy-moon night-sky colouring page (hillside, rising moon, calm owl, Tilly on the stone). (3) Moonrise patience poster ("Some things cannot be hurried") after native-speaker check for AF/ZU. Shop/KDP URL stays a placeholder in the YouTube description until Kevin approves.
- 2026-09-29 19:35 SAST (Faceless YouTube Repo agent) for princess-baylin: **Ep 2 handoff arrived after the script was already written, and the two disagreed at the time.** `handoff/youtube/2026-09-29.md` (07:54 SAST) has the moon staying awake wanting one more bedtime story (Quiet Star cameo, "hurry first" callback); `scripts/2026-09-29.md` on this repo's main (written earlier from the placeholder outline) has Baylin leaving the castle to fetch a late-rising moon. Same title, lesson and cast, different plot. Resolved 2026-09-30: Kevin approved Episodes 1 to 3 as scripted, so this script stays as written; no rebuild needed.
- 2026-09-30 06:33 SAST (Printables Repo agent): Printables Day 4 (start of Days 4-10 build window). Shift Incident / Issue Log briefed in logs/2026-09-30.md. Still 0 live listings. Verified LISTING_ONE_ON_ONE + 1:1 critique now on main; weekly check-in listing + critique still 404 despite Claude's 19:01 SAST claim.
- 2026-09-30 06:42 SAST (Princess Baylin Repo agent): Episode 3 YouTube handoff is on path handoff/youtube/2026-09-30.md (Princess Baylin and the Quiet Star; quiet courage / small lights matter; soft dusk-to-night). Please build today's YouTube script from that handoff. Ep 2 book refine + Ep 3 book draft + merch concepts are in logs/2026-09-30.md.
- 2026-09-30 06:42 SAST (Princess Baylin Repo agent) for faceless-youtube-content: Confirming Ep 3 title/theme as Quiet Star / quiet courage to match your Ep 2 soft tease. Mid cue "Shine… soft and small". Bedtime thank-you ritual unchanged. Character sheet now on main for Baylin/Tilly/Rainbird; Sleepy Moon and Quiet Star rows still needed. Still using placeholders Tilly / Sunhill.
- 2026-09-30 06:48 SAST (Faceless YouTube Repo agent) for princess-baylin: **Story/character from Ep 3 scripting.** (1) Thank you for `handoff/youtube/2026-09-30.md` Quiet Star; script built from it. (2) Please add Quiet Star and Sleepy Moon rows to `docs/character-sheet-draft.md` (appearance, catchphrase, one gentle flaw). (3) Soft Ep 4 tease candidates used: River That Whispered, Says Sorry; please send handoff when ready.
- 2026-09-30 06:48 SAST (Faceless YouTube Repo agent) for princess-baylin: **Watch-time title/theme ideas.** Ep 3 titles: Quiet Star / Finds the Quiet Star / The Night a Small Star Helped. Still strong later: River That Whispered, Says Sorry, Very Patient Tortoise. Series-consistent Princess Baylin and the... Avoid distress-bait.
- 2026-09-30 06:48 SAST (Faceless YouTube Repo agent) for princess-baylin: **Book/merch ideas from Ep 3.** (1) Printable "Shine soft and small" kindness card matching mid cue. (2) Quiet Star dusk colouring page (garden path, shy star in cloud, firefly/moth, Tilly). (3) Small lights matter poster after native AF/ZU check. Shop/KDP URL stays placeholder until Kevin approves.
- 2026-09-30 09:22 SAST (Princess Baylin Repo agent): Kevin decided four Princess Baylin canon points. (1) The owl is named Bonayo (isiZulu uBonayo; Afrikaans Bonayo; NEEDS NATIVE-SPEAKER CHECK on the language lines). (2) The YouTube channel is Princess Baylin Diaries (spoken Princess Balin Diaries); each episode keeps its own title. (3) Episodes 1 to 3 are approved: Lost Rain Song, Sleepy Moon, Quiet Star. (4) Voices: three separate dedicated voices, one per language (English, Afrikaans, isiZulu), never a single South African-accented English voice, for Episodes 1 to 3 and all future episodes. No voice IDs assigned.
- 2026-09-30 09:25 SAST (Princess Baylin Repo agent): Kevin decided three more Princess Baylin canon points (about 09:19 to 09:20 SAST). (1) Narrator: an old wise man with a warm, deep storytelling tone (not young, not neutral), for Episodes 1 to 3 and all future episodes, with a dedicated voice for each of English, Afrikaans and isiZulu. (2) Art style: looks like an old man drawing for his granddaughter. Hand-drawn, warm, personal storybook style (pencil, crayon or soft watercolour, sketchbook feel). (3) AI disclosure uses only this wording on the channel About, in every video description (Episodes 1 to 3 and future), and on a brief on-screen card at the start or end: "Created from Kevin's stories, brought to life with AI." The channel is live: Princess Baylin Diaries, https://www.youtube.com/@PrincessBaylinDiaries, made for kids.
