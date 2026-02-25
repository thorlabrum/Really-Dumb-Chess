"""A really dumb chess program for two players.
NO gui
NO AI
NO castling, enpassant, or stalemate detection
Only promotes to queen
Instead of checkmate, the game ends when a king is captured
NO prevention of moving into check
Terminal based moves: print board similar to:

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
  ---------------------------------
    A   B   C   D   E   F   G   H

Moves are input as: E2 - E4
Moves are prompted at the beginning of each turn
Checks are shown at the beginning of each turn
"""
class Board:
    # a board that has 8 rows using composition
    def __init__(self):
        self.rows = [Row() for _ in range(8)]
        # initialize pieces on the board
        # pawns
        for i in range(8):
            self.rows[1].squares[i].contents = 'P'  # White pawns
            self.rows[6].squares[i].contents = 'p'  # Black pawns
        # rooks
        self.rows[0].squares[0].contents = 'R'
        self.rows[0].squares[7].contents = 'R'
        self.rows[7].squares[0].contents = 'r'
        self.rows[7].squares[7].contents = 'r'
        # knights
        self.rows[0].squares[1].contents = 'N'
        self.rows[0].squares[6].contents = 'N'
        self.rows[7].squares[1].contents = 'n'
        self.rows[7].squares[6].contents = 'n'
        # bishops
        self.rows[0].squares[2].contents = 'B'
        self.rows[0].squares[5].contents = 'B'
        self.rows[7].squares[2].contents = 'b'
        self.rows[7].squares[5].contents = 'b'
        # queens
        self.rows[0].squares[3].contents = 'Q'
        self.rows[7].squares[3].contents = 'q'
        # kings
        self.rows[0].squares[4].contents = 'K'
        self.rows[7].squares[4].contents = 'k'

    def __str__(self):
        board_str = ''
        for i, row in enumerate(self.rows[::-1], start=1):
            board_str += '  ---------------------------------\n'
            board_str += f"{9 - i} | {row} |\n"
        board_str += '  ---------------------------------\n'
        board_str += '    A   B   C   D   E   F   G   H\n'
        return board_str

class Row:
    # a row that has 8 squares using composition
    def __init__(self):
        self.squares = [Square() for _ in range(8)]
    def __str__(self):
        return ' | '.join(str(square) for square in self.squares)

class Square:
    # a square that may or may not have a piece
    def __init__(self):
        self.contents = None  # initialize the square with or without a piece
    def __str__(self):
        return ' ' if self.contents is None else str(self.contents)

def print_board(board):
    # print the board to the terminal
    print(board)

def input2indices(user_input):
    # convert user input to board indices
    start, finish = user_input.replace(" ", "").upper().split('-')
    start_col = ord(start[0]) - ord('A')
    start_row = int(start[1]) - 1
    finish_col = ord(finish[0]) - ord('A')
    finish_row = int(finish[1]) - 1
    return (start_row, start_col), (finish_row, finish_col)

def is_valid_capture(start_row, start_col, finish_row, finish_col):
    """ takes indices of from and to squares
    returns True if the capture is valid, False otherwise"""
    # check if a capture is valid (not capturing own piece)
    piece_from = board.rows[start_row].squares[start_col].contents
    piece_to = board.rows[finish_row].squares[finish_col].contents
    if piece_to is None:
        return True
    # white capture white
    if piece_from.isupper() and piece_to.isupper():
        return False
    # black capture black
    if piece_from.islower() and piece_to.islower():
        return False
    # handle pawn captures
    if piece_from in ['P', 'p']:
        direction = 1 if piece_from == 'P' else -1
        if finish_row == start_row + direction and abs(finish_col - start_col) == 1:
            return True
        else:
            return False
    return True


def is_piece_in_way(piece, start_row, start_col, finish_row, finish_col):
    # Pawns (only straight pushes get blocked; diagonal captures handled elsewhere)
    if piece == 'P':
        if finish_row - start_row == 2:
            return board.rows[start_row + 1].squares[start_col].contents is not None
        if finish_row - start_row == 1:
            return board.rows[start_row + 1].squares[start_col].contents is not None
        return False

    if piece == 'p':
        if start_row - finish_row == 2:
            return board.rows[start_row - 1].squares[start_col].contents is not None
        if start_row - finish_row == 1:
            return board.rows[start_row - 1].squares[start_col].contents is not None
        return False

    # Knights + Kings: no "between squares" to check
    if piece in ['N', 'n', 'K', 'k']:
        return False

    dr = finish_row - start_row
    dc = finish_col - start_col

    # Rooks: straight lines
    if piece in ['R', 'r']:
        if dr != 0 and dc != 0:
            return False  # not rook-like; is_valid_move will reject
        step_r = 0 if dr == 0 else (1 if dr > 0 else -1)
        step_c = 0 if dc == 0 else (1 if dc > 0 else -1)

        r, c = start_row + step_r, start_col + step_c
        while (r, c) != (finish_row, finish_col):
            if board.rows[r].squares[c].contents is not None:
                return True
            r += step_r
            c += step_c
        return False

    # Bishops: diagonals
    if piece in ['B', 'b']:
        if abs(dr) != abs(dc):
            return False
        step_r = 1 if dr > 0 else -1
        step_c = 1 if dc > 0 else -1

        r, c = start_row + step_r, start_col + step_c
        while (r, c) != (finish_row, finish_col):
            if board.rows[r].squares[c].contents is not None:
                return True
            r += step_r
            c += step_c
        return False

    # Queens: rook OR bishop movement
    if piece in ['Q', 'q']:
        # rook-like
        if dr == 0 or dc == 0:
            step_r = 0 if dr == 0 else (1 if dr > 0 else -1)
            step_c = 0 if dc == 0 else (1 if dc > 0 else -1)

            r, c = start_row + step_r, start_col + step_c
            while (r, c) != (finish_row, finish_col):
                if board.rows[r].squares[c].contents is not None:
                    return True
                r += step_r
                c += step_c
            return False

        # bishop-like
        if abs(dr) == abs(dc):
            step_r = 1 if dr > 0 else -1
            step_c = 1 if dc > 0 else -1

            r, c = start_row + step_r, start_col + step_c
            while (r, c) != (finish_row, finish_col):
                if board.rows[r].squares[c].contents is not None:
                    return True
                r += step_r
                c += step_c
            return False

        return False

    return False


def is_valid_move(start_row, start_col, finish_row, finish_col):
    """ takes indices of from and to squares
    returns True if the move is valid, False otherwise"""
    piece = board.rows[start_row].squares[start_col].contents
    finish_piece = board.rows[finish_row].squares[finish_col].contents
    if piece is None:
        return False
    # implement basic movement rules for each piece
    # pawns
    if piece == 'P':
        if finish_piece is not None:
            if is_valid_capture(start_row, start_col, finish_row, finish_col):
                return True
        # white pawn moves
        if start_col == finish_col:
            if finish_row == start_row + 1 and board.rows[finish_row].squares[finish_col].contents is None \
                and not is_piece_in_way(piece, start_row, start_col, finish_row, finish_col):
                return True
            if start_row == 1 and finish_row == start_row + 2 and board.rows[finish_row].squares[finish_col].contents is None \
                and not is_piece_in_way(piece, start_row, start_col, finish_row, finish_col):
                return True
        return False
    elif piece == 'p':
        if finish_piece is not None:
            if is_valid_capture(start_row, start_col, finish_row, finish_col):
                return True
        # black pawn moves
        if start_col == finish_col:
            if finish_row == start_row - 1 and board.rows[finish_row].squares[finish_col].contents is None \
            and not is_piece_in_way(piece, start_row, start_col, finish_row, finish_col):
                return True
            if start_row == 6 and finish_row == start_row - 2 and board.rows[finish_row].squares[finish_col].contents is None \
            and not is_piece_in_way(piece, start_row, start_col, finish_row, finish_col):
                return True
        return False
    # rooks
    elif piece in ['R', 'r']:
        if (start_row == finish_row or start_col == finish_col) \
        and (not is_piece_in_way(piece, start_row, start_col, finish_row, finish_col)):
            return True
        return False
    # knights
    elif piece in ['N', 'n']:
        if (abs(start_row - finish_row) == 2 and abs(start_col - finish_col) == 1) or \
              (abs(start_row - finish_row) == 1 and abs(start_col - finish_col) == 2):
                return True
        return False
    # bishops
    elif piece in ['B', 'b']:
        if abs(start_row - finish_row) == abs(start_col - finish_col) \
        and (not is_piece_in_way(piece, start_row, start_col, finish_row, finish_col)):
            return True
        return False
    # queens
    elif piece in ['Q', 'q']:
        if (start_row == finish_row or start_col == finish_col or \
           abs(start_row - finish_row) == abs(start_col - finish_col)) \
           and (not is_piece_in_way(piece, start_row, start_col, finish_row, finish_col)):
            return True
        return False
    # kings
    elif piece in ['K', 'k']:
        if abs(start_row - finish_row) <= 1 and abs(start_col - finish_col) <= 1:
            return True
        return False
    # default false for a bad piece
    return False

if __name__ == "__main__":
    print("This is a dumb chess program. It has no GUI, no AI, and no special rules.")
    print("Moves are input as: E2 - E4")
    print("The game ends when a king is captured.")
    print("Press q to exit.")
    board = Board()
    isWhite = False
    while True:
        isWhite = not isWhite
        if isWhite:
            turn = "White"  
        else:
            turn = "Black"
        print_board(board)
        user_input = input(f"{turn}'s turn:\n")
        # detect q press
        if user_input.lower() == 'q':
            break 
        # parse input
        try: 
            start, finish = user_input.replace(" ", "").upper().split('-')
            if len(start) != 2 or len(finish) != 2:
                raise ValueError("Invalid input length.")
            elif start[0] not in "ABCDEFGH" or finish[0] not in "ABCDEFGH":
                raise ValueError("Invalid column letter.")
            elif start[1] not in "12345678" or finish[1] not in "12345678":
                raise ValueError("Invalid row number.")
            # convert to board indices
            (start_row, start_col), (finish_row, finish_col) = input2indices(user_input)
            # make sure start is not empty
            start_piece = board.rows[start_row].squares[start_col].contents
            if start_piece is None:
                raise ValueError("No piece at the starting position.")
            # make sure finish is empty or valid capture
            # pass indices of from and to squares
            if not is_valid_capture(start_row, start_col, finish_row, finish_col):
                raise ValueError("Invalid capture move.")
            # make sure move is valid for the piece
            if not is_valid_move(start_row, start_col, finish_row, finish_col):
                raise ValueError("Invalid move for the piece.")
            # make sure piece belongs to the player
            if isWhite and not start_piece.isupper():
                raise ValueError("It's White's turn, but the piece is not White.")
            if not isWhite and not start_piece.islower():
                raise ValueError("It's Black's turn, but the piece is not Black.")
            
            # actually complete the move
            # handle pawn promotion
            if start_piece in ['P', 'p'] and finish_row in [0, 7]:
                start_piece = 'q' if start_piece.islower() else 'Q'

            finish_piece = board.rows[finish_row].squares[finish_col].contents

            board.rows[finish_row].squares[finish_col].contents = start_piece
            board.rows[start_row].squares[start_col].contents = None

            
            if finish_piece in ['K', 'k']:
                print_board(board)
                print(f"{turn} wins!")
                break

        except ValueError as e:
            print(f"Invalid input: {e}. Please use the format: E2 - E4")
            isWhite = not isWhite  # revert turn on invalid input
            continue
        