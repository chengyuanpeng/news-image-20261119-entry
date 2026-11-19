# The World in One Day

[![Competition](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/chengyuanpeng/news-image-20261119-entry/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/chengyuanpeng/news-image-20261119-entry/reward.svg)](https://make.fun/bounty/news-image-20261119)

A newspaper-style illustrated summary of six major world stories from Thursday 19 November 2026, with a culture strip marking the worldwide launch of Grand Theft Auto VI.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program uses Pillow and the bundled fonts to create `out/entry.png`. In the make.fun runner, the harness supplies the output directory.

## Stories shown

- The first US–China–Russia trilateral summit and its peace declaration
- The International Court of Justice ruling on Myanmar and the Rohingya
- Israel's ground operation in central Gaza after the October 2025 ceasefire
- Houthi missile attacks damaging Riyadh's PIF tower
- The magnitude 5.7 Kumamoto earthquake, with no tsunami
- Nvidia's $115.8 billion quarter and Anthropic's Nasdaq debut

The image is generated entirely with local code and bundled assets. It makes no network requests.
