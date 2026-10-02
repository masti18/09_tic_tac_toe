# Tic-Tac-Toe Lab — Lab 4 Solution

Python/Pygame Tic-Tac-Toe completed according to the Lab 4 requirements.

## Completed tasks

1. **Win/draw detection:** all 8 winning lines are checked; wins are evaluated before a draw; input is locked after a round ends.
2. **Persistent scoreboard:** X wins, O wins, and draws persist across round restarts and clear only on a match reset.
3. **Move validation:** occupied cells are rejected without changing the board or current turn.
4. **First-player choice and separate restarts:** X/O selects the first player for the next round; `R` restarts the round while keeping scores; `M` resets the entire match.

## Run

```bash
pip install -r requirements.txt
python main.py
```

## Controls

- Click an empty board cell: place X when it is your turn.
- `X`: choose X as first player for the next round.
- `O`: choose O as first player for the next round.
- `R`: restart the current round and keep the scoreboard.
- `M`: reset the entire match and clear the scoreboard.
