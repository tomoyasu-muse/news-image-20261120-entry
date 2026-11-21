# 20 November 2026 — The World in One Day

[![make.fun bounty](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/tomoyasu-muse/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/tomoyasu-muse/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120)

A program that writes one image summing up the world news of
**Friday 20 November 2026** to `/output/entry.png`, entered in the
[make.fun bounty "Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120).

## What the image shows

A newspaper front page with the date **20 NOVEMBER 2026** in large
type and six stories, cross-checked across several news sources:

- Russia's massive drone and missile attack on Kyiv, with missiles landing in Poland
- The ICJ ruling that Myanmar committed genocide against the Rohingya
- Trump, Xi and Putin issuing a joint peace pledge after the Shenzhen summit
- COP31 climate talks in Antalya stalling over fossil fuels
- The UK and EU agreeing a new trade and youth mobility deal in Brussels
- US AI stocks sliding as Anthropic lists on Nasdaq

## How it works

`entry.png` is drawn by `draw_entry.py` (Python + Pillow) before
submission. `main.py` (Python 3.13, standard library only) copies
that finished image to `/output/entry.png`, so two runs in the
offline grading sandbox always write exactly the same bytes.

Run it locally:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
