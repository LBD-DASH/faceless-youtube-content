# Scripts index

Updated 2026-11-14. One row per episode. The slate (titles, lessons, dates, story shapes) lives in princess-baylin `docs/100-video-slate.md` and `docs/100-video-slate.csv`.

## Story episodes

| Episode | Title | Render from | Status on 2026-11-14 |
|---|---|---|---|
| 1 | Princess Baylin and the Lost Rain Song | `2026-10-04.md` (production pack; original script `2026-09-28.md`) | Live: https://www.youtube.com/watch?v=BrF_v5ACTxo |
| 2 | Princess Baylin and the Sleepy Moon | `2026-10-05.md` (production pack; original script `2026-09-29.md`) | Script approved 2026-09-30. Render requested from Grok Bot 2026-11-14 |
| 3 | Princess Baylin and the Quiet Star | `2026-10-06.md` (production pack; original script `2026-09-30.md`) | Script approved 2026-09-30. Render requested from Grok Bot 2026-11-14. The lost creature is a firefly, and the last shot gets the silent Bonayo sketch |
| 4 | Princess Baylin and the River That Whispered | `2026-10-01.md` | Approved 2026-11-14 with fixes applied |
| 5 | Princess Baylin and the Very Patient Tortoise | `2026-10-02.md` | Approved 2026-11-14 with fixes and a new opening |
| 6 | Princess Baylin and the Market of Small Kindnesses | `2026-10-03.md` | Approved 2026-11-14 with fixes and a new opening |
| 7 | Princess Baylin and the Thank-You Lantern | `2026-11-14-ep7-thank-you-lantern.md` | Written and approved for art 2026-11-14 |
| 8 | Princess Baylin and the Gift That Could Not Be Wrapped | `2026-11-14-ep8-gift-that-could-not-be-wrapped.md` | Written and approved for art 2026-11-14 |
| 9 | Princess Baylin and the Knot That Grew | not written | Next to write |
| 10 | Princess Baylin and the Day That Did Not Want to End | not written | Next to write |

Episodes 11 to 40 are in the slate and not written yet. Claude writes them two a week, in slate order, by the steps in `docs/weekly-script-run.md`. The daily agent does not write new episode scripts.

## Calm Minute Shorts

`calm-minute-shorts.md` holds SH01 to SH08. From Episode 4 onward each episode file also carries its own Calm Minute Short. Add each new Short to both places.

## Other files

- `drafts/`: shot boards for Episodes 1 to 3 and the Episode 2 outline.
- `check_pace.py`: run it on every script before committing. `python3 scripts/check_pace.py scripts/<file>.md`
- `run_prompts.py`: the prompt runner for `prompts/`. It is not used for scripts.

## Rules for a new script

1. Name it `YYYY-MM-DD-epNN-short-title.md` (the date it was written). The six October files keep their date-only names.
2. Build it from the slate row and follow `docs/channel-style-guide.md`. Use `2026-11-14-ep8-gift-that-could-not-be-wrapped.md` as the model for layout.
3. The story must not repeat the situation and outcome of an earlier episode. Say how it differs in its Originality check.
4. `check_pace.py` must print ALL OK.
5. Add the row here, update the slate row in princess-baylin (`status` and `script_file`), and write the handoff in princess-baylin `handoff/youtube/`.
6. The planning timestamps in Episodes 1 to 3 are tighter than a calm read. The real chapter times for those three come from the render.

Nothing here is for publish until Kevin has watched the finished video. Afrikaans and isiZulu wait for a named native-speaker reviewer.
