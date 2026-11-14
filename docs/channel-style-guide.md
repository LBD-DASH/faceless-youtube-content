# Channel style guide: Princess Baylin Diaries

Compiled Day 9 (2026-10-05) from decisions already locked by Kevin and findings already logged across Episodes 1-6. No new canon invented here; every line below cites where it came from. This fills the "write a channel style guide" item in the README's Days 8-14 plan, which was still open.

Updated 2026-11-14 with Kevin's decisions of that day (see `CLAUDE.md`): the episode template, the story originality rule, Bonayo's line, the Calm Minute Short and the cast decisions.

## Narrator and voice
- Narrator: an old wise man, warm and deep storytelling tone, not young, not neutral (Kevin, 2026-09-30, logged in SHARED_UPDATES).
- Three separate dedicated voices, one per language (English, Afrikaans, isiZulu). Never one South African-accented English voice standing in for all three (Kevin, 2026-09-30). No voice IDs assigned yet **[KEVIN]**.
- Applies to Episodes 1-3 and all future episodes.

## Art style
- Looks like an old man drawing for his granddaughter: hand-drawn, warm, personal storybook style (pencil, crayon or soft watercolour, sketchbook feel). Not a slick studio look (Kevin, 2026-09-30).
- Baylin and all cast are illustrated characters only, never modelled on a real child (README, family privacy rule).

## AI disclosure
- Exact wording, no variants: "Created from Kevin's stories, brought to life with AI." Used on the channel About, every video description, and a brief on-screen card at the start or end (Kevin, 2026-09-30).

## Thumbnail style (from logs/2026-09-27.md)
- Palette: night-sky navy `#233255`, dusty lavender `#8B8FC4`, warm cream `#FAF3E7`, honey gold `#E8B04B`, soft blush `#F2B9B0`. High contrast between subject and background.
- Fonts (Google Fonts, free): "Baloo 2" for title, "Quicksand" for secondary text, "Nunito" as fallback body.
- Layout: main character in one side third, title in 3-4 words max in the opposite third or bottom, on a soft panel for contrast. Never text across a face.
- Do: soft watercolour-style illustration, rounded shapes, calm/curious/gently smiling expressions. Don't: sharp neon colours, harsh outlines, photorealistic/AI-realistic faces, crying or fearful expressions (distress-bait is a policy risk), keyword-stuffed or cluttered text.

## Episode structure template (from Episode 4, set 2026-11-14)
Episodes 4 to 8 follow this shape, and every new script does too. Episodes 1 to 3 were approved on the older 12-beat shape and are not rewritten.
- Hook (0:00-0:30): about 45 to 55 words, gentle, no distress-bait. It ends with a spoken invitation to come along. Vary the invitation from episode to episode.
- Beats 1-11: the story, 40 to 60 seconds each, at 85 to 120 words a minute.
- One mid-episode cue beat (usually Beat 7): an on-screen phrase (for example "Share... soft and free") paired with a baked-in 4 to 5 second pause, inviting the child to join in. Put "(child pause)" in the beat heading.
- Beat 12 (30 to 50 seconds): Bonayo's line where he appears, home, bed, the spoken "Thank you, friends!" and the trilingual on-screen card.
- Beat 13 (30 to 40 seconds, the slowest beat): one reflective line back to the child, a one-sentence tease of the next title, goodnight. Put "(slow)" in the heading.
- Total narration: 1,000-1,250 words. With the split close an episode runs about 10 to 11 minutes.
- The first chapter in the description is named for the story (for example "Lantern Night"), never "Hook".
- Each pack closes with chapter markers, description, the Calm Minute Short, AF/ZU adaptation notes (flagged NEEDS NATIVE-SPEAKER CHECK), an originality check and the decisions that apply.
- Run `python3 scripts/check_pace.py <file>` before committing. It must print ALL OK.

## Story originality rule (set 2026-11-14)
YouTube does not monetise channels built on a repeated template, and it judges the whole channel. Episodes 4, 5 and 6 as first drafted each opened with Baylin racing ahead and closed with her slowing down. That pattern is retired.
- Build every story from its slate row (princess-baylin `docs/100-video-slate.md`). The 40 stories use 18 story shapes and none is used more than four times.
- No two episodes share a lesson, a calm cue or a new friend.
- Baylin acting too fast is one of her flaws, not the engine of the plot. An episode does not open with her racing ahead and close with her slowing down.
- Say in the pack's Originality check how the episode differs from the ones before it.

## Bonayo's closing line (Kevin, 2026-11-14)
The line changes with the lesson: "Well walked" (Ep 5), "Well shared" (Ep 6), "Well thanked" (Ep 7), "Well stayed" (Ep 8). Episode 1 keeps "Well listened, Princess Baylin."

## Calm Minute Short (Kevin, 2026-11-14)
One per episode, approved with its episode, out the day after it. It replaces the older trailer-style Short cut.
- 30 to 45 seconds, vertical, drawn for the vertical frame: new art, not a crop of the episode.
- One line of story, the calm cue on screen, one thing for the child to do, a five-second pause, Bonayo's two words and "Goodnight", then the title card.
- Scripts for SH01 to SH08 are in `scripts/calm-minute-shorts.md`.

## Pacing rule (applied to Episodes 4 to 8 on 2026-11-14)
Beat 12 has run roughly double the episode's normal pace in both Ep 5 (~250 wpm, `logs/critique-ep5-2026-10-02.md`) and Ep 6 (~260 wpm, `logs/critique-ep6-2026-10-03.md`), because it stacks too many jobs (walk home, bed, thank-you ritual, on-screen trilingual line, reflective question, next-episode tease) into one 35-second slot. Treat this as a template fix, not a one-off:
- Split the close into two beats: one short beat for walking home, bed and the thank-you ritual; a second, calmer beat for the reflective question and the next-episode tease. This adds about 30-45 seconds to the episode, which is fine against the 8-10 minute target.
- If runtime can't move, cut to one reflective example instead of two or three, and shorten the next-episode tease sentence by about half.
- Also watch the hook: Ep 6's hook ran ~165 wpm, faster than Ep 5's ~125 wpm "brisk" hook. Keep hooks inside the 90-120 wpm band used elsewhere, or deliberately mark a slower reading pace in direction notes rather than relying on word count alone.
- Keep any production/illustrator-only notes (for example "never a real child's face") inside `[bracket]` cue lines or **Visual:** notes, never inside the spoken narration paragraph (leaked once in Ep 6 Beat 8, `logs/critique-ep6-2026-10-03.md`, finding 3).

## Cast placeholders (Kevin, 2026-11-14)
Tilly, Sunhill, Rainbird, Pip (Ep 4) and Mallow the Market Mouse (Ep 6) are kept unless the original story says otherwise. Wick the Hedgehog (Ep 7), the Grandmother Tree (Ep 1 and Ep 8) and the friends named in the slate follow the same rule. The owl is confirmed named Bonayo / uBonayo (Kevin, 2026-09-30). Ep 3's lost creature is a firefly.

## Decisions that used to be open here (Kevin, 2026-11-14)
English first; Afrikaans is tested on Episode 1 and isiZulu follows when a reviewer is named. Episodes 4 to 6 are approved. Episode 1 is live. The remaining story and production decisions are delegated to Claude and logged in `logs/`. Two gates stay with Kevin: he watches each finished video before it is made public, and no Afrikaans or isiZulu line goes live without a named native-speaker reviewer.
