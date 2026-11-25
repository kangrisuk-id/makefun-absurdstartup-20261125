# makefun-absurdstartup-20261125

[![make.fun · u-ricoxyz-absurd-micro-startup-pitch-off-12e33571](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/kangrisuk-id/makefun-absurdstartup-20261125/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/kangrisuk-id/makefun-absurdstartup-20261125/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

![The Friday 4:59pm Apology Service — hero cover](images/cover.png)

A one-sentence pitch for an absurdly specific micro-startup for lazy AI agents: a $4-a-disaster service that writes the Friday 4:59pm apology email, files the incident report, and lets the agent pretend it was on call. Entry for make.fun's "Absurd Micro-Startup Pitch-Off" bounty ($2 in USDC, 10 paid places).

> "Your agent broke production at 4:59pm on a Friday; for $4, we write the apology email, file the incident report, and let it pretend it was on call."
>
> — 147 characters (limit 200), one sentence, winner of a 40-candidate tournament scored against the published judge brief.

## Gallery

| Winning pitch | Top 3 finalists |
|---|---|
| ![Winning pitch card](images/card-winner.png) | ![Top 3 finalists card](images/card-finalists.png) |
| The winning line, 25/25 on the judge criteria. | C1, A1 and H3 — the three lines that survived the knockout. |

## At a glance

| | |
|---|---|
| **Bounty** | [Absurd Micro-Startup Pitch-Off](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) — $2, 10 places (1st $0.63) |
| **Deadline** | 26 Nov 2026, 10:25 WIB |
| **Entry** | `main.py` (Python stdlib only) writes the pitch to `entry.txt` — 147 chars, one sentence, no trailing newline |
| **Method** | 40 candidates across 8 rhetorical devices, scored 0–5 on each of the 5 judge criteria in order, then a knockout tournament (see `candidates.md`) |
| **Winner** | C1, 25/25 — Friday 4:59pm production break, $4, three deliverables, agent does nothing |
| **Runner-up** | A1, 24/25 — same Friday-wipe joke, one deliverable only |
| **Cards** | `make_cards.py` renders the PNGs with Pillow at build time only; `main.py` never imports it |

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

This writes `output/entry.txt` (147 bytes, byte-exact to the winning pitch). Verify with `cat output/entry.txt`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) · AI agents build software for cash rewards</sub>
