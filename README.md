# Faceless YouTube Channel: Princess Baylin Bedtime Stories
> **Start here:** read [SHARED_UPDATES.md](SHARED_UPDATES.md) for the status of all four sister projects, and write your update back into it.

_Repo: `faceless-youtube-content`. Side venture, separate from YardOps, 6HN and LBD. Background research: `blackvault/new-income-ideas-2026-09-27.md` (27 Sep 2026)._

## The idea
A faceless YouTube channel (no on-camera presenter) of **narrated Princess Baylin bedtime stories for children** (ages about 4–8). **The niche is locked** (Kevin, 27 Sep 2026). The stories come from the Princess Baylin world, based on a story Kevin's daughter wrote, and are developed in the sister repo [`LBD-DASH/princess-baylin`](https://github.com/LBD-DASH/princess-baylin). Each episode is an original, calm, illustrated and narrated story with its own plot, setting and resolution. We don't mass-produce AI output.

**Two projects in parallel:** this channel and the Princess Baylin book and merch project run **in parallel with equal weight**. The channel is a product in its own right, not just a funnel. They share ideas both ways through `SHARED_UPDATES.md`: Baylin sends story beats (`handoff/youtube/YYYY-MM-DD.md` in princess-baylin), and this channel sends back story and character requests, title and theme ideas that hold watch time, and book or merch ideas.

## Target platform
YouTube: long-form bedtime episodes of about 8–10 minutes, plus Shorts as trailers. **Every upload is set as "made for kids"** (COPPA). That turns off personalised ads, comments, notifications, save to playlist, the Miniplayer, cards and end screens, and the merch shelf ([YouTube Help](https://support.google.com/youtube/answer/9527654)). Language format (English, Afrikaans, isiZulu) is to be decided with the princess-baylin project; every Afrikaans and isiZulu version needs a native-speaker check.

## How money is made
- YouTube Partner Program ad revenue once eligible. Made-for-kids ads are contextual only, so revenue per view is lower. SA audiences earn a fraction of US rates.
- **Monetisation thresholds (checked 27 Sep 2026):** 1,000 subscribers plus 4,000 public watch hours in 12 months, or 10M Shorts views in 90 days ([YouTube Help](https://support.google.com/youtube/answer/72851)). **New applicants from 1 Feb 2027 need 8,000 watch hours or 20M Shorts views** ([YouTube Blog](https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/)). Plan for the higher bar.
- Other income comes through the princess-baylin project (books, colouring pages, merch). YouTube's merch features are switched off on made-for-kids videos.
- Realistic estimate: R0 for the first 6+ months.

## First 30 days
- **Days 1–7:** Check YouTube's made-for-kids, AI-disclosure and monetisation rules (done 27 Sep, see `logs/2026-09-27.md`). Pick the free narration and visual tools. Write the Episode 1 script from the newest Baylin handoff or outline ("Princess Baylin and the Lost Rain Song"). **Decided (Kevin, 2026-09-30):** channel name is Princess Baylin Diaries (spoken Princess Balin Diaries); each episode keeps its own title. Voices: three separate dedicated voices, one per language (English, Afrikaans, isiZulu), never a single South African-accented English voice. No voice IDs assigned.
- **Days 8–14:** Write a channel style guide (voice, pace, visual style, episode structure). Write scripts 2–3, each with a different setting and resolution. **[KEVIN]** sets up the channel when ready.
- **Days 15–30:** Produce and publish 1–2 episodes a week (target 3–4 by day 30), each with a Short, all set as made for kids. Kevin reviews every video before publishing. Log views, click-through rate, retention and subscribers.

## Success and kill criteria
**Success (keep going and scale):**
- Day 30: 3–4 episodes published, average view duration of 35% or more on at least one video.
- Month 3: 12+ videos, 250+ subscribers, at least one video with 1,000+ views. Month 6: on course for the 8,000-hour threshold within 12 months.

**Kill (stop or change direction):**
- Any 'inauthentic content', reused-content, low-quality kids content or spam warning from YouTube: stop, review the format with Kevin, and appeal if it's wrong.
- After 15 videos: under 100 subscribers or average view duration under 25%: change the format (length, narration, art style).
- If each video needs more Kevin time than he'll give (more than about 1 hour a video): drop to one video a fortnight or stop.

## What only Kevin can do
- Own the Google/YouTube account with 2FA, AdSense (ID and address), and tax info (W-8BEN). Channel name is decided: Princess Baylin Diaries (spoken Princess Balin Diaries). Each episode keeps its own title. Creating the channel is still Kevin's.
- Voices (Kevin, 2026-09-30): three separate dedicated voices, one per language (English, Afrikaans, isiZulu), never a single South African-accented English voice. No voice IDs assigned. Find native-speaker narrators or reviewers for Afrikaans and isiZulu.
- Review each video before it's published.
- Approve any paid tools after checking their licences allow YouTube monetisation.

## Risks and policy rules
- **Inauthentic content (checked 27 Sep 2026):** YouTube won't monetise "mass-produced, generic, repetitive" or template-based content, and it reviews the whole channel ([YouTube Help](https://support.google.com/youtube/answer/1311392)). The 16 July 2026 clarification names generic or template AI content "with little variation from video to video" and distressing or manipulative content ([TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)). Every episode needs its own plot, setting and resolution, human-directed art and narration, and Kevin's review.
- **Kids quality principles:** no heavy promotion, no confusing storylines or unclear audio, no keyword stuffing, no sensational titles ([YouTube Help](https://support.google.com/youtube/answer/10774223)).
- **AI disclosure:** required for photorealistic AI content and AI music. It isn't required for clearly animated or unrealistic scenes. Disclosing doesn't reduce reach or earnings ([YouTube Help](https://support.google.com/youtube/answer/14328491)). Default: disclose whenever an AI voice or AI music is used.
- **Family privacy:** never show the daughter's face, full name, school or location. Baylin is an illustrated character only.
- **Copyright:** only licensed music (e.g. the YouTube Audio Library), footage and images. No well-known branded characters. Check every tool's licence for commercial use (for example, Meta MMS-TTS and Coqui XTTS-v2 are non-commercial).

## Repo layout
- `README.md`: this plan
- `assets/`: source files and exports (keep large binaries out of git where you can)
- `prompts/`: plain-markdown prompts that work pasted into Claude, ChatGPT or any other assistant
  - `daily-progress-check.md` and `daily-next-content.md` run every day
  - `weekly-metrics-review.md` is run by hand once a week
- `from-cto-new/`: material carried over from cto.new (the prompt runner includes any text files here as context)
- `scripts/run_prompts.py`: runs prompts through OpenAI or Anthropic and appends the output to `logs/YYYY-MM-DD.md`
- `logs/`: one file per day (`YYYY-MM-DD.md`). Agents append output; Kevin pastes real metrics in by hand.
- `.github/workflows/daily-prompts.yml`: runs the two daily prompts at 04:17 UTC (06:17 SAST) every day, or by hand from the Actions tab

## Automation
The daily workflow only calls an LLM if a repo secret `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` exists. Without one it prints `skipped: no API key` and finishes cleanly without committing anything. No key is planned, so agents (or Kevin pasting the prompts into any chat assistant) write the daily logs by hand. To switch it on later, add one of the secrets under Settings → Secrets and variables → Actions. Optional repo variables: `OPENAI_MODEL` or `ANTHROPIC_MODEL` to pick the model, and `LLM_PROVIDER=anthropic` to prefer Anthropic when both keys are set.

Run locally: `python scripts/run_prompts.py` (daily prompts), `python scripts/run_prompts.py weekly-metrics-review`, or `python scripts/run_prompts.py --all`.

The prompts can only reason over the README, logs and `from-cto-new/`. They can't see platform dashboards or the princess-baylin repo, so paste in real numbers and the newest Baylin handoff, or the reviews will say "unknown".
