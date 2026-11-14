#!/usr/bin/env python3
"""Check the pace of an episode script before it is committed.

Usage:
    python3 scripts/check_pace.py scripts/2026-11-14-ep8-gift-that-could-not-be-wrapped.md [more files]

For every beat heading of the form "### [0:30-1:20] Beat 1 - Name" it counts the
spoken words under the heading and prints words, seconds and words per minute.
Sound cues in [brackets], **Visual:** notes, tables and rules are not counted.
A beat whose heading contains "child pause" has 5 seconds taken off its time.

It fails (exit code 1) when:
- a beat reads slower than 85 or faster than 120 words a minute,
- the beat times do not join up, or the first beat does not start at 0:00,
- the narration total is outside 1,000 to 1,250 words,
- the file contains an em dash, an en dash, curly quotes or a stray @ sign.

Standard library only. Added 2026-11-14 with the channel style guide update.
"""
import re
import sys

TIME = re.compile(r"\[(\d+:\d\d)-(\d+:\d\d)\]")
# Built from code points so that this file holds none of the characters itself.
BANNED = {chr(0x2014): "em dash", chr(0x2013): "en dash", chr(0x201C): "curly quote",
          chr(0x201D): "curly quote", chr(0x2018): "curly quote", chr(0x2019): "curly quote"}
CHANNEL = "youtube.com/@PrincessBaylinDiaries"
LOW, HIGH = 85, 120
MIN_WORDS, MAX_WORDS = 1000, 1250
SKIP = ("[", "**Visual", "---", "|", "### ")


def seconds(stamp):
    minutes, secs = stamp.split(":")
    return int(minutes) * 60 + int(secs)


def beats_of(text):
    """Return [heading, spoken word count] for each timed beat."""
    beats, current = [], None
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("### ") and TIME.search(s):
            current = [s[4:], 0]
            beats.append(current)
            continue
        if s.startswith("## ") or s.startswith("# "):
            current = None
            continue
        if current is None or not s or s.startswith(SKIP):
            continue
        current[1] += len(s.split())
    return beats


def check(path):
    text = open(path, encoding="utf-8").read()
    beats = beats_of(text)
    problems = []
    print(f"== {path}")
    if not beats:
        print("   no timed beats found")
        return False
    previous_end = 0
    for heading, words in beats:
        match = TIME.search(heading)
        start, end = seconds(match.group(1)), seconds(match.group(2))
        if start != previous_end:
            problems.append(f"times do not join up before: {heading}")
        previous_end = end
        spoken = end - start - (5 if "child pause" in heading else 0)
        if spoken <= 0:
            problems.append(f"no time in: {heading}")
            continue
        wpm = words / (spoken / 60)
        flag = ""
        if not LOW <= wpm <= HIGH:
            flag = f"  <-- outside {LOW} to {HIGH}"
            problems.append(f"{wpm:.0f} wpm in: {heading}")
        print(f"   {words:4d} words {end - start:3d}s {wpm:5.0f} wpm  {heading}{flag}")
    total = sum(words for _, words in beats)
    print(f"   total {total} words in {len(beats)} beats, ends {previous_end // 60}:{previous_end % 60:02d}")
    if not MIN_WORDS <= total <= MAX_WORDS:
        problems.append(f"narration is {total} words, outside {MIN_WORDS} to {MAX_WORDS}")
    for char, name in BANNED.items():
        if char in text:
            problems.append(f"file contains a {name}")
    if "@" in text.replace(CHANNEL, ""):
        problems.append("file contains an @ sign outside the channel URL")
    for problem in problems:
        print(f"   PROBLEM: {problem}")
    return not problems


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    results = [check(path) for path in sys.argv[1:]]
    print("ALL OK" if all(results) else "PROBLEMS FOUND")
    sys.exit(0 if all(results) else 1)
