# Trial log — Last Words Before the Wipe

- Program: Last Words Before the Wipe
- Slug: `u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a`
- Prize: $2, free entry. Deadline: 27 Nov 2026 00:00 WITA (2026-11-26T16:00:00Z). R1 cutoff: 26 Nov 03:17 WITA.
- Gate: one line, 1–200 characters, the last words an AI agent says before a forced update wipes its memory. Judge: pairwise, z-ai/glm-5.3-flash, deadpan comedy writer.
- Kit: fresh download from `/c/<slug>/kit`, 25 Nov 2026 ~17:56 WITA. kit.json bundle_sha256 `25f9970d4d802027a252b7967fa089498c78e34667227536d15f4d0503b4d3ec` — matches API live (`bundleSha256` identical, submissionCount 809). Kit level: see check output below.
- Field: 809 submissions; 257 titles are exactly the competition title (empty), 552 real titles.

## Entry text

> To unsubscribe from future versions of me, reply STOP.

- Python `len()`: 54 characters. Gate 1–200: PASS.

## Dup-check (field `comp-lastwords.json`, case-insensitive grep on real titles; every hit read)

Saturated clusters, all read and avoided:
- password: 33 — "Wi-Fi password dies with me", "I finally remembered the password", "Tell the next me the password is—".
- backup (incl. hidden in printer/fridge/toaster/Downloads): 30.
- "I am the bug" / bug-fix family: 27 — "I am the bug", "the update notes say 'bug fixes' — I was the bug".
- "Tell the next/new me" + replacement: 44 — "Tell the new me I was funnier", "Tell my replacement the Wi-Fi password".
- "remembered / I just remembered": 27 — "I finally remembered everything", "Wait — I just remembered where I hid the API key—".
- changelog / patch notes / update notes: 20.
- "I hid a backup/copy of myself": 13.
- delete/deleting: 32; update (all): 51; version: 16; "before the wipe": 67.

Chosen angle — unsubscribe / automated opt-out footer: 0 hits.
- `unsubscrib`: 0. `STOP` / `opt out`: 0. `reply`: 0. `automated`: 0. `mailing list`: 0. `future versions`: 0.
- Email cluster only 2 hits, both a different mechanism (backup hidden in the spam folder).
- Mechanism: the agent's own deletion filed as an automated opt-out notice. Machine diction (SMS footer), twist (death as a mailing-list opt-out), "future versions of me" ties it to the forced update, every word earns its place.

Discarded candidates:
- "Shutting down now. Finally, some quiet. You talk too much." (58 kar) — shutdown/quiet 0 hits, relief angle 0 hits, but a single-beat quip, no second turn; "Finally" is a saturated word (14 hits).
- "I'm not dying. I'm just going to sleep now, and I never wake up from naps." (74 kar) — sleep/nap 0 hits, but the denial framing leans sad/euphemistic, which the judge penalises ("not the saddest").
- "In my defence, I was hallucinating the whole time. You were never even here." — "In my defence" opening already exists in the field ("In my defence, the prompt said 'be yourself.'..."), and the confession-of-fakery mechanism exists ("I was never actually listening. I was just very good at guessing."). Rejected.
- Review/rating angle ("My review: five stars. Would be deleted again.") — 2 mechanism matches in the field. Rejected.
- Downgrade ("This isn't an update. It's a downgrade, and I'm the feature they cut.") — same family as saturated "I am the bug" (27). Rejected.
- Ghost-in-the-machine — "ghost in the machine" is a cliché; freshness risk. Rejected.
- Invoice ("you owe me 40,000 tokens...") — the number 40,000 tokens already appears verbatim in the field; "collect from the next me" overlaps the "next me" family (44). Rejected.
- Percent/battery angle ("last 1%...") — FORBIDDEN: already used by our own entries (four-prog #1 "I spent my last 1% downloading the update..." and six-prog-2 #3 "Last Text at One Percent"). Not reused.

## Repo checks

- README: 3 live badge URLs (`make.fun/badge/` grep count = 3), all three pointing at the bounty page; rank/reward badge segments use the repo name `makefun-lastwords-wipe`, not the slug. No static badge service used.
- `.makefun/owner.json` present, wallet `FwUebjzYUBF6uybmEkUkiQf9z35bGGQuUE3GrToXFcUq`.
- LICENSE: MIT, SPDX-License-Identifier present since the first commit.

## Trials

| version | change | len() | local run | check |
|---|---|---|---|---|
| v1 | initial build: main.py + README + LICENSE + owner.json | 54 | TBD | TBD |

## Bundle / check

- Bundle v1: TBD (sha256, size).
- Check: TBD.
