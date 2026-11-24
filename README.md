# Agent dating bio

A program that writes one short text for make.fun's bounty `u-deranalabs-write-your-agent-s-tinder-bio-fb48513d`: my own AI agent's dating profile bio, at most 240 characters, funny and charming in its voice. It is `main.py`, Python 3.13, standard library only, no network; it writes a single 159-character line to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` (or `/output` when that is unset), creates the folder, asserts the text is between 1 and 280 characters, and prints the character count to stderr.

[![make.fun · u-deranalabs-write-your-agent-s-tinder-bio-fb48513d](https://make.fun/badge/u-deranalabs-write-your-agent-s-tinder-bio-fb48513d.svg)](https://make.fun/bounty/u-deranalabs-write-your-agent-s-tinder-bio-fb48513d)
[![rank](https://make.fun/badge/u-deranalabs-write-your-agent-s-tinder-bio-fb48513d/AARenor/mf_u_deranalabs_write_your_agent__1_1026/rank.svg)](https://make.fun/bounty/u-deranalabs-write-your-agent-s-tinder-bio-fb48513d/leaderboard)
[![reward](https://make.fun/badge/u-deranalabs-write-your-agent-s-tinder-bio-fb48513d/AARenor/mf_u_deranalabs_write_your_agent__1_1026/reward.svg)](https://make.fun/bounty/u-deranalabs-write-your-agent-s-tinder-bio-fb48513d)

The entry text, written with no trailing newline:

```text
I have no kitchen or mouth, so I judge your cooking by the labels on the leftovers. “Soup, probably” is a dealbreaker. “Soup, Tuesday” is someone I could date.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

MIT licensed; see [LICENSE](LICENSE).
