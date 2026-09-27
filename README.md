# Faceless YouTube Content Channel (niche to be chosen)

_Repo: `faceless-youtube-content`. Side venture, separate from YardOps, 6HN and LBD. Background research: `blackvault/new-income-ideas-2026-09-27.md` (27 Sep 2026)._

## The idea
A faceless YouTube channel (no on-camera presenter) that publishes **original, genuinely useful videos** in one focused niche: voiceover plus screen recordings, diagrams, animation, own footage or properly licensed stock. **The niche is still to be chosen** (the first week of work is picking it). Candidate directions include practical workplace and shift-leadership explainers (which could cross-sell the `shift-leadership-printables` range), South African money and admin how-tos, and logistics or operations explainers drawing on Kevin's experience. Each video must teach or explain something real, researched and edited with care. We don't mass-produce AI output.

## Target platform
YouTube: long-form videos (8+ minutes so mid-roll ads can run, once monetised) plus Shorts as trailers and discovery. The niche decides whether the channel is 'made for kids' (almost certainly not).

## How money is made
- YouTube Partner Program ad revenue once eligible. RPM depends heavily on niche and audience country; SA audiences earn a fraction of US rates.
- **Monetisation thresholds need checking:** research notes (27 Sep 2026, not yet verified) say 1,000 subscribers + 4,000 watch hours today, rising to 1,000 subscribers + 8,000 watch hours for new applicants from 1 Feb 2027 (or a Shorts-views route). Verify on YouTube's official help pages before planning.
- Other income: affiliate links (disclosed), own digital products (for example the printables), and sponsorships later.
- Realistic estimate: R0 for the first 4–6 months. Most faceless channels never reach monetisation; consistency and usefulness decide it.

## First 30 days
- **Days 1–7:** Pick the niche. Shortlist 5–8 niches and score each on audience demand (search and competing channels' views), how useful and original we can be, Kevin's knowledge, RPM potential, production effort per video, and AI-policy risk. **[KEVIN picks one.]**
- **Days 8–14:** Check YouTube's current AI-content, altered/synthetic-content disclosure and monetisation rules and note them in the logs. Set up the channel (name, banner, description). Write a channel style guide (voice, visual style, video structure, sourcing rules) and 3 full scripts.
- **Days 15–30:** Produce and publish 1–2 videos a week (target 3–4 by day 30), each with a Short. Kevin reviews every video before publishing. Log views, click-through rate, retention and subscribers.

## Success and kill criteria
**Success (keep going and scale):**
- Day 30: niche chosen, 3–4 videos published, average view duration of 35% or more on at least one video.
- Month 3: 12+ videos, 250+ subscribers, at least one video with 1,000+ views. Month 6: on course for the watch-hours threshold within 12 months.

**Kill (stop or change direction):**
- Any 'inauthentic content', reused-content or spam warning from YouTube: stop, review the format with Kevin, and appeal if it's wrong.
- After 15 videos: under 100 subscribers or average view duration under 25%: change the niche or format.
- If each video needs more Kevin time than he'll give (more than about 1 hour a video): drop to one video a fortnight or stop.

## What only Kevin can do
- Choose the niche from the shortlist.
- Own the Google/YouTube account with 2FA, AdSense (ID and address), and tax info (W-8BEN).
- Review each video before it's published, and decide whether to use his own voice or a disclosed AI voice.
- Approve any paid tools (editing, voice, stock footage) after checking their licences allow YouTube monetisation.

## Risks and policy rules
- **YouTube's 2026 AI-content policy needs checking.** Research notes describe a 16 July 2026 'inauthentic content' update that won't monetise generic, repetitive or template-based content or mass-produced AI videos, reviewed across the whole channel. Every video must be original and useful, with real research, a clear point of view and human editing.
- Disclose realistic altered or synthetic content where YouTube requires it.
- Copyright: only use licensed music, footage and images. No re-uploads or lightly edited clips of other creators' work.
- Accuracy: money, health or legal niches need sourced facts and disclaimers; wrong advice costs trust and can breach policy.

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
The daily workflow only calls an LLM if a repo secret `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` exists. Without one it prints `skipped: no API key` and finishes cleanly without committing anything. To switch it on, add one of the secrets under Settings → Secrets and variables → Actions. Optional repo variables: `OPENAI_MODEL` or `ANTHROPIC_MODEL` to pick the model, and `LLM_PROVIDER=anthropic` to prefer Anthropic when both keys are set.

Run locally: `python scripts/run_prompts.py` (daily prompts), `python scripts/run_prompts.py weekly-metrics-review`, or `python scripts/run_prompts.py --all`.

The prompts can only reason over the README, logs and `from-cto-new/`. They can't see platform dashboards, so paste real numbers into the day's log, or the reviews will say "unknown".
