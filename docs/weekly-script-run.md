# Weekly script run

How Claude writes the week's two Princess Baylin episode scripts. Set on 2026-11-14 under Kevin's delegation. Any Claude session can follow it when Kevin asks for the week's scripts. It is not scheduled yet: a weekly scheduled run needs Kevin's own approval, and he was asked on 2026-11-14.

The daily repo agents do not write new episode scripts or handoffs for new episodes. That keeps one voice across the series and avoids two agents writing the same episode.

## Limits

- Never publish, upload, schedule or post anything. Never email or message anyone. Never spend money. Never open or edit `.env` files or secrets.
- Both repos are public. No em dashes or en dashes, no curly quotes, no email addresses, nothing that identifies a real child, and nothing about Kevin's other ventures.
- Afrikaans lines are drafts flagged NEEDS NATIVE-SPEAKER CHECK. No isiZulu drafts: they come from a native-speaker reviewer.
- A script marked approved is cleared for art and the English render only. Nothing goes public until Kevin has watched the finished video.
- Do not edit the approved scripts of earlier episodes.

## Steps

1. **Pull.** `git pull --rebase` in princess-baylin and faceless-youtube-content.
2. **Read.** `CLAUDE.md` in both repos. In princess-baylin: `docs/100-video-slate.md` and `.csv`, `docs/series-bible-draft.md`, `docs/character-sheet-draft.md`, the newest log and the newest handoff. Here: `docs/channel-style-guide.md`, `scripts/README.md`, the Episode 7 and 8 scripts (the models for layout, voice and quality) and the two most recent scripts. If princess-baylin `assets/story/` holds the original story, read it: it is canon and it overrules the slate.
3. **Choose.** The two lowest-numbered story episodes with no script yet (status Idea in the slate).
4. **Write** each as `scripts/YYYY-MM-DD-epNN-short-title.md`, laid out like `scripts/2026-11-14-ep8-gift-that-could-not-be-wrapped.md`.
   - Build it from the slate row: lesson, new friend, setting, premise, calm cue and story shape. Keep the cue wording exactly.
   - A 30-second hook and 13 beats, 1,000 to 1,250 words. One calm cue beat with a child pause. Beat 12 holds Bonayo's line, home, bed and the thank-you card. Beat 13 is the reflective line, a one-sentence tease of the next title and goodnight.
   - Bonayo's line is "Well" plus one word that fits the lesson, then her name.
   - A different story from every earlier episode, in situation and in outcome. Do not reuse the opening image, turning point or closing image of the four scripts before it.
   - Gentle throughout. The turn comes from a friend's question or a small discovery, not from a lecture.
   - Reread it twice as a demanding children's editor: once for story logic, once aloud for rhythm.
   - `python3 scripts/check_pace.py <file>` must print ALL OK.
5. **Record here.** Add each Calm Minute Short to `scripts/calm-minute-shorts.md`, add the rows to `scripts/README.md`, and write `logs/YYYY-MM-DD.md` with word counts, run times and every decision made.
6. **Record in princess-baylin.** Write `handoff/youtube/YYYY-MM-DD.md` in the form of `handoff/youtube/2026-11-14.md`. Set the episodes and their Shorts to Script approved in `docs/100-video-slate.csv` and `docs/100-video-slate.md`, with `script_file` filled in. Add each new friend to `docs/character-sheet-draft.md` and each episode to "Episodes so far" in `docs/series-bible-draft.md`. Write `logs/YYYY-MM-DD.md`. Update the Princess Baylin and Faceless YouTube sections of `SHARED_UPDATES.md`, identical in both repos.
7. **Scoreboard.** Append one dated row to princess-baylin `logs/scoreboard.md`: subscribers, total views, number of videos and views per video, read from public YouTube data. Watch hours and average view duration need YouTube Studio: write "not available" unless Kevin or Grok Bot has supplied them. Check the figures against the stop rules in princess-baylin `docs/series-plan-100.md`.
8. **Commit and push** small commits with clear messages. Never force-push.
9. **Kevin's Sheet.** Set the same rows to Script approved in Kevin's private slate Sheet. Kevin holds the link.

End with a five-line summary: what was written, files changed, commits pushed, anything Kevin must decide, and next week's two episodes.
