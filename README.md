# tiny-chess-01-v3

A chess engine in under 4 KB of Python (main.py). 64-square board with
precomputed attack tables, iterative-deepening alpha-beta search with
principal-variation search, a 1M-entry transposition table, null-move
pruning, late-move reductions, check extensions, killer/history move
ordering, and a quiescence search over captures, promotions and check
evasions. Evaluation is a tapered material + piece-square score with
pawn-structure terms (passed, doubled, isolated pawns) memoised per pawn
configuration, bishop pair, and mate-distance scoring so won positions
are converted by the shortest forced line. Search runs on a fixed node
budget — fully deterministic, no wall clock in move choice — and
repetition and the 50-move rule score as draws inside the search.

## Run

python3 main.py — the engine connects to the environment at
MAKEFUN_ENV_URL, asks for its next game, replays the move list, searches
and posts each move back until the game ends.

## Built with

Built with [make.fun](https://make.fun) — referral code: 9j3w1sg2
