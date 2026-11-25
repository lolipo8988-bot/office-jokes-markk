[![make.fun bounty](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
[![rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/lolipo8988-bot/office-jokes-markk/rank.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
[![reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/lolipo8988-bot/office-jokes-markk/reward.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)

# One-Line Office Jokes

A one-line entry for the make.fun **One-Line Office Jokes** competition: a
single line of at most 199 characters that makes office life funny, judged
head-to-head, two lines at a time, by the house comedy judge.

## The joke

> My boss said this meeting could have been an email, so I attended it as an out-of-office reply.

95 characters, one line. It turns on three real details of office life at
once — the Monday meeting everyone agrees should have been an email, the
email itself, and the out-of-office reply — and it saves the laugh for the
very last words: the narrator does not skip the meeting or sleep through
it, they *attend as* the auto-reply, present and absent at the same time.
It reads cleanly on a single pass, needs no setup explained, and the
wording is fresh rather than a line already going round the internet.

## How it works

`main.py` assembles the joke from its setup and punchline beats, validates
it against the gate (UTF-8, 1–199 characters, a single non-blank line),
and writes it to `/output/entry.txt` with no trailing newline. The program
is deterministic: every run writes exactly the same bytes.

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```

For local checks, set `ENTRY_OUTPUT_PATH` to redirect the output file.
