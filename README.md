# Really-Dumb-Chess

A really dumb chess program for two players.

## Features (or lack thereof)
- **NO GUI** - Terminal-based only
- **NO AI** - Two human players only
- **NO castling, en passant, or stalemate detection**
- **NO prevention of moving into check**
- Only promotes pawns to queens
- Game ends when a king is captured (not checkmate)

## How to Play

Run the program:
```bash
python chess.py
```

The board is displayed in the terminal like this:
```
  ---------------------------------
8 | r | n | b | q | k | b | n | r |
  ---------------------------------
7 | p | p | p | p | p | p | p | p |
  ---------------------------------
6 |   |   |   |   |   |   |   |   |
  ---------------------------------
5 |   |   |   |   |   |   |   |   |
  ---------------------------------
4 |   |   |   |   |   |   |   |   |
  ---------------------------------
3 |   |   |   |   |   |   |   |   |
  ---------------------------------
2 | P | P | P | P | P | P | P | P |
  ---------------------------------
1 | R | N | B | Q | K | B | N | R |
  ---------------------------------
    A   B   C   D   E   F   G   H
```

- **Uppercase letters** = White pieces
- **Lowercase letters** = Black pieces
- **P/p** = Pawn, **R/r** = Rook, **N/n** = Knight, **B/b** = Bishop, **Q/q** = Queen, **K/k** = King

## Move Input

Moves are input in the format: `E2 - E4`

- First coordinate = starting position
- Second coordinate = destination position
- Press `q` to exit the game

## Piece Movement

The program implements basic movement rules for all pieces:
- **Pawns**: Move forward 1 square (or 2 from starting position), capture diagonally
- **Rooks**: Move horizontally or vertically
- **Knights**: Move in L-shape (2 squares in one direction, 1 in perpendicular)
- **Bishops**: Move diagonally
- **Queens**: Move horizontally, vertically, or diagonally
- **Kings**: Move 1 square in any direction

## Example Game

```
White's turn:
E2 - E4
Black's turn:
E7 - E5
```

Enjoy your really dumb chess game!