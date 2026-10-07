# Episode production checklist: from approved script to upload-ready file

Compiled Day 10 (2026-10-06). Nothing in the repo yet walked through the actual production steps (record, illustrate, assemble, publish) end to end, and the README's Day 15-30 window (produce and publish 1-2 episodes a week) starts in 5 days with zero production started. This checklist only assembles tools and rules already decided or logged; it invents no new canon and does not start production itself. Use it once Kevin greenlights Episode 1 (or any later episode) for production.

## 0. Before starting
- [ ] **[KEVIN]** Episode greenlit for production? (see SHARED_UPDATES open decision)
- [ ] Placeholders for this episode confirmed or still flagged pending (check `docs/channel-style-guide.md` cast placeholders list)
- [ ] AF/ZU lines for this episode still marked NEEDS NATIVE-SPEAKER CHECK until a named reviewer signs off (no publish of AF/ZU on-screen text or VO before then)

## 1. Narration (English first, per locked voice decision)
- [ ] Record English narration per `scripts/YYYY-MM-DD.md`, old-wise-man warm/deep tone, in **Audacity** (free, GPL) — tool choice logged in `logs/2026-09-27.md`
- [ ] Apply the pacing fix from `docs/channel-style-guide.md` close-beat rule: split beat 12 into two slower beats rather than reading it at normal speed
- [ ] Afrikaans / isiZulu narration: hold for a named native-speaker narrator per voice (never one accented English voice standing in for all three); do not use Meta MMS-TTS or Coqui XTTS-v2 (both non-commercial licences, per `logs/2026-09-27.md`)

## 2. Art
- [ ] Build or reuse Baylin's fixed character sheet (coordinate with princess-baylin's `docs/character-sheet-draft.md`) so the episode matches prior episodes
- [ ] Illustrate the episode's scenes in **Krita** (free, GPL) following the 12-scene shot list / visual plan in the episode's script or production pack
- [ ] Match the locked art style: hand-drawn, warm, personal storybook feel (pencil, crayon or soft watercolour); never a slick studio look; never a real child's likeness
- [ ] Build the thumbnail per `docs/channel-style-guide.md` thumbnail style (palette, fonts, layout, do/don't list)

## 3. Assembly
- [ ] Animate gentle pan/zoom over stills in **Blender** (Grease Pencil) if any light motion is wanted; stills with slow pan/zoom are enough for v1 per the production pack
- [ ] Edit in **Kdenlive**, **Shotcut**, or **DaVinci Resolve** (free tier) — sync narration to visuals, add chapter markers from the script's timestamp table
- [ ] Add music/SFX only from the **YouTube Audio Library**; add Creative Commons attribution in the description if the track requires it; avoid AI-generated music, or disclose it if used
- [ ] Add the on-screen AI disclosure card: exactly "Created from Kevin's stories, brought to life with AI."
- [ ] Add captions (at least English)

## 4. Upload settings
- [ ] Set **made for kids** (COPPA) — this turns off personalised ads, comments, cards, end screens, and the merch shelf; expected, not a bug
- [ ] Paste title (pick from the script's 3 calm options), description, and chapter markers from the production pack
- [ ] Add tags from the production pack's keyword list (tags only, never stuffed into the title)
- [ ] Confirm AI disclosure text is also in the description and (if required) the About page
- [ ] Final **[KEVIN]** review of the finished video before publish (README requirement: Kevin reviews every video before publishing)

## 5. After publish
- [ ] Log the upload date in `logs/YYYY-MM-DD.md`
- [ ] Start tracking views, impressions CTR, average view duration, subscribers, and watch hours in the next weekly metrics review — these are the numbers the Day-30 success/kill criteria depend on
