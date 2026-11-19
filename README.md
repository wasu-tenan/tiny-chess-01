# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/wasu-tenan/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/wasu-tenan/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in exactly 4,096 bytes of Python (standard library only). 0x88 board, full legal move generation (castling, en passant, promotions; perft-verified against python-chess), alpha-beta search with quiescence, transposition-table move ordering, a history heuristic and check extensions, under a deterministic fixed node budget. It plays through the make.fun environment's HTTP/JSON protocol, answering each position with a UCI move. Local gauntlet vs the practice anchors: ≈1,191 Elo.

## Run it

```sh
MAKEFUN_ENV_URL=<environment-url> python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=2mmz0hmg&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
