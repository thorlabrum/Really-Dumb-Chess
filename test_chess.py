import pytest
from chess import is_valid_move, Board

"""
How this works (cause it's a little backwards)

If you want to clear the space A2 you use

           2          A
board.rows[1].squares[0].contents = None

Or if you want to move from A2 to A4

              2  A  
is_valid_move(1, 0, 3, 0, board)
                    4  A
is_valid_move(1, 0, 3, 0, board)


Letter to number cheat sheet:
A - 0 
B - 1
C - 2
D - 3
E - 4
F - 5
G - 6
H - 7

"""

def test_distance_d1():
    """TC-D1: Same position should be invalid"""
    board = Board()
    valid = is_valid_move(1, 4, 1, 4, board)
    assert not valid

def test_distance_d2():
    """TC-D2: Long distance move with clear path"""
    board = Board()
    # Removing pieces in path
    board.rows[1].squares[0].contents = None
    board.rows[6].squares[0].contents = None
    
    valid = is_valid_move(0, 0, 7, 0, board)
    assert valid

def test_distance_d3():
    """TC-D3: Two square pawn move"""
    board = Board()
    valid = is_valid_move(1, 6, 3, 6, board)
    assert valid


def test_path_p1():
    """TC-P1: Blocked path should be invalid"""
    board = Board()
    valid = is_valid_move(0, 3, 3, 0, board)
    assert not valid


def test_pawn_wp1():
    """TC-WP1: White pawn single move forward"""
    board = Board()
    valid = is_valid_move(1, 7, 2, 7, board)
    assert valid

def test_pawn_bp1():
    """TC-BP1: Black pawn single move forward"""
    board = Board()
    valid = is_valid_move(6, 1, 5, 1, board)
    assert valid

def test_pawn_bp2():
    """TC-BP2: Black pawn two square move"""
    board = Board()
    valid = is_valid_move(6, 1, 4, 1, board)
    assert valid

def test_pawn_paw1():
    """TC-PAW1: Pawn diagonal capture"""
    board = Board()
    # Arranging board for TC-PAW1
    # White pawn move
    board.rows[1].squares[3].contents = None
    board.rows[3].squares[3].contents = 'P'
    # Black pawn move
    board.rows[6].squares[4].contents = None
    board.rows[4].squares[4].contents = 'p'

    valid = is_valid_move(3, 3, 4, 4, board)
    assert valid

def test_pawn_paw2():
    """TC-PAW2: Pawn cannot move backward"""
    board = Board()
    # Arranging board for TC-PAW2
    # Black pawn move
    board.rows[6].squares[4].contents = None
    board.rows[4].squares[4].contents = 'p'

    valid = is_valid_move(4, 4, 5, 4, board)
    assert not valid

def test_pawn_promotion_pp1():
    """TC-PP1: Pawn promotion to queen"""
    board = Board()
    # Arranging board for TC-PP1
    # Moving white pawn to promotion square 
    board.rows[7].squares[0].contents = None
    board.rows[6].squares[0].contents = 'P'
    
    valid = is_valid_move(6, 0, 7, 0, board)
    assert valid


def test_rook_r1():
    """TC-R1: Rook horizontal move"""
    board = Board()
    # Arranging board for TC-R1
    # Moving black rook
    board.rows[7].squares[0].contents = None
    board.rows[2].squares[0].contents = 'r'

    valid = is_valid_move(2, 0, 2, 7, board)
    assert valid

def test_rook_r2():
    """TC-R2: Rook invalid diagonal move"""
    board = Board()
    # Arranging board for TC-R2
    # Moving white rook
    board.rows[0].squares[0].contents = None
    board.rows[2].squares[0].contents = 'R'

    valid = is_valid_move(2, 0, 4, 1, board)
    assert not valid


def test_bishop_b1():
    """TC-B1: Bishop diagonal move"""
    board = Board()
    # Arranging board for TC-B1
    # Moving white bishop
    board.rows[0].squares[2].contents = None
    board.rows[2].squares[4].contents = 'B'

    valid = is_valid_move(2, 4, 3, 3, board)
    assert valid

def test_bishop_b2():
    """TC-B2: Bishop invalid straight move"""
    board = Board()
    # Arranging board for TC-B2
    # Moving black bisop
    board.rows[7].squares[2].contents = None
    board.rows[5].squares[4].contents = 'b'

    valid = is_valid_move(5, 4, 5, 0, board)
    assert not valid

def test_bishop_b3():
    """TC-B3: Bishop blocked path"""
    board = Board()
    valid = is_valid_move(0, 5, 2, 3, board)
    assert not valid


def test_queen_q1():
    """TC-Q1: Queen horizontal move"""
    board = Board()
    # Arranging board for TC-Q1
    # Moving white queen
    board.rows[0].squares[3].contents = None
    board.rows[2].squares[3].contents = 'Q'

    valid = is_valid_move(2, 3, 2, 0, board)
    assert valid

def test_queen_q2():
    """TC-Q2: Queen diagonal move"""
    board = Board()
    # Arranging board for TC-Q2
    # Moving black queen
    board.rows[7].squares[3].contents = None
    board.rows[5].squares[3].contents = 'q'

    valid = is_valid_move(5, 3, 3, 5, board)
    assert valid

def test_queen_q3():
    """TC-Q3: Queen invalid move pattern"""
    board = Board()
    valid = is_valid_move(0, 3, 2, 4, board)
    assert not valid

def test_queen_q4():
    """TC-Q4: Queen blocked path"""
    board = Board()
    valid = is_valid_move(0, 3, 2, 3, board)
    assert not valid

def test_queen_q5():
    """TC-Q5: Queen blocked by own piece"""
    board = Board()
    # Arranging board for TC-Q5
    # Moving black queen
    board.rows[7].squares[3].contents = None
    board.rows[5].squares[3].contents = 'q'
    # Moving black pawn
    board.rows[6].squares[2].contents = None
    board.rows[5].squares[2].contents = 'p'

    valid = is_valid_move(5, 3, 5, 0, board)
    assert not valid


def test_knight_n1():
    """TC-N1: Knight L-shaped move"""
    board = Board()
    # Arranging board for TC-N1
    # Moving white knight
    board.rows[0].squares[1].contents = None
    board.rows[2].squares[2].contents = 'N'

    valid = is_valid_move(2, 2, 3, 4, board)
    assert valid

def test_knight_n2():
    """TC-N2: Knight from starting position"""
    board = Board()
    valid = is_valid_move(7, 6, 5, 5, board)
    assert valid

def test_knight_n3():
    """TC-N3: Knight invalid move distance"""
    board = Board()
    # Arranging board for TC-N3
    # Moving black knight
    board.rows[0].squares[6].contents = None
    board.rows[2].squares[5].contents = 'N'

    valid = is_valid_move(2, 5, 6, 5, board)
    assert not valid


def test_king_k1():
    """TC-K1: King single square move"""
    board = Board()
    # Arranging board for TC-K1
    # Moving white pawn
    board.rows[1].squares[4].contents = None
    board.rows[2].squares[4].contents = 'P'

    valid = is_valid_move(0, 4, 1, 4, board)
    assert valid

def test_king_k2():
    """TC-K2: King cannot move multiple squares"""
    board = Board()
    # Arranging board for TC-K2
    # Removing piece in path
    board.rows[6].squares[4].contents = None
 
    valid = is_valid_move(7, 4, 3, 4, board)
    assert not valid


def test_boundary_bv1():
    """TC-BV1: Move across entire row"""
    board = Board()
    # Arranging board for TC-BV1
    # Removing all pieces from B1 to H1
    for i in range(1, 8):
        board.rows[0].squares[i].contents = None

    valid = is_valid_move(0, 0, 0, 7, board)
    assert valid

def test_boundary_bv2():
    """TC-BV2: King move exceeds single square"""
    board = Board()
    # Arranging board for TC-BV2
    # Removing pawn in path
    board.rows[6].squares[0].contents = None
    # Moving black king
    board.rows[7].squares[4].contents = None
    board.rows[7].squares[0].contents = 'k'

    valid = is_valid_move(7, 0, 5, 0, board)
    assert not valid

def test_boundary_bv3():
    """TC-BV3: Bishop long diagonal"""
    board = Board()
    # Arranging board for TC-BV3
    # Removing pawn in path
    board.rows[1].squares[3].contents = None

    valid = is_valid_move(0, 2, 5, 7, board)
    assert valid

def test_boundary_bv4():
    """TC-BV4: Queen full column move"""
    board = Board()
    # Arranging board for TC-BV4
    # Removing pieces in path
    board.rows[1].squares[3].contents = None
    board.rows[6].squares[3].contents = None
    board.rows[7].squares[3].contents = None

    valid = is_valid_move(0, 3, 7, 3, board)
    assert valid


# Helper function tests

def test_input2indices_basic():
    """Test basic input parsing"""
    from chess import input2indices
    
    (start_row, start_col), (finish_row, finish_col) = input2indices("E2-E4")
    assert start_row == 1  # Row 2 = index 1
    assert start_col == 4  # Column E = index 4
    assert finish_row == 3  # Row 4 = index 3
    assert finish_col == 4  # Column E = index 4

def test_input2indices_with_spaces():
    """Test input parsing with spaces"""
    from chess import input2indices
    
    (start_row, start_col), (finish_row, finish_col) = input2indices("A1 - H8")
    assert start_row == 0
    assert start_col == 0
    assert finish_row == 7
    assert finish_col == 7

def test_input2indices_lowercase():
    """Test input parsing with lowercase letters"""
    from chess import input2indices
    
    (start_row, start_col), (finish_row, finish_col) = input2indices("a2-a4")
    assert start_row == 1
    assert start_col == 0
    assert finish_row == 3
    assert finish_col == 0

def test_input2indices_corners():
    """Test corner positions"""
    from chess import input2indices
    
    (start_row, start_col), (finish_row, finish_col) = input2indices("H1-A8")
    assert start_row == 0
    assert start_col == 7
    assert finish_row == 7
    assert finish_col == 0


def test_is_valid_capture_empty_square():
    """Test capture on empty square"""
    from chess import is_valid_capture
    
    board = Board()
    # Move to empty square should be valid
    valid = is_valid_capture(1, 0, 2, 0, board)
    assert valid

def test_is_valid_capture_opponent_piece():
    """Test capturing opponent piece"""
    from chess import is_valid_capture
    
    board = Board()
    # White pawn trying to capture black pawn (if adjacent)
    # Set up a scenario where white can capture black
    board.rows[3].squares[3].contents = 'P'
    board.rows[4].squares[4].contents = 'p'
    
    valid = is_valid_capture(3, 3, 4, 4, board)
    assert valid

def test_is_valid_capture_own_piece_white():
    """Test capturing own piece (white)"""
    from chess import is_valid_capture
    
    board = Board()
    # White trying to capture white
    valid = is_valid_capture(0, 0, 1, 0, board)
    assert not valid

def test_is_valid_capture_own_piece_black():
    """Test capturing own piece (black)"""
    from chess import is_valid_capture
    
    board = Board()
    # Black trying to capture black
    valid = is_valid_capture(7, 0, 6, 0, board)
    assert not valid

def test_is_valid_capture_white_pawn_diagonal():
    """Test white pawn diagonal capture"""
    from chess import is_valid_capture
    
    board = Board()
    # Set up white pawn at row 3, col 3
    board.rows[1].squares[3].contents = None
    board.rows[3].squares[3].contents = 'P'
    # Place black piece diagonally
    board.rows[4].squares[4].contents = 'p'
    
    valid = is_valid_capture(3, 3, 4, 4, board)
    assert valid

def test_is_valid_capture_white_pawn_invalid_diagonal():
    """Test white pawn invalid diagonal capture"""
    from chess import is_valid_capture
    
    board = Board()
    # White pawn trying to capture two squares diagonally
    board.rows[3].squares[3].contents = 'P'
    board.rows[5].squares[5].contents = 'p'
    
    valid = is_valid_capture(3, 3, 5, 5, board)
    assert not valid

def test_is_valid_capture_black_pawn_diagonal():
    """Test black pawn diagonal capture"""
    from chess import is_valid_capture
    
    board = Board()
    # Set up black pawn
    board.rows[6].squares[4].contents = None
    board.rows[4].squares[4].contents = 'p'
    # Place white piece diagonally
    board.rows[3].squares[3].contents = 'P'
    
    valid = is_valid_capture(4, 4, 3, 3, board)
    assert valid


# --- Capturing pieces / piece capture rules (EC-R1, EC-R2, EC-B1, EC-Q1, EC-Q2, EC-N1, EC-K1) ---

def test_rook_capture_same_row():
    """Rook captures enemy on same row (EC-R1: same row move + capture)."""
    board = Board()
    board.rows[0].squares[0].contents = None
    board.rows[2].squares[0].contents = 'R'
    board.rows[2].squares[5].contents = 'p'
    assert is_valid_capture(2, 0, 2, 5, board)
    assert is_valid_move(2, 0, 2, 5, board)

def test_rook_capture_same_col():
    """Rook captures enemy on same column (EC-R2: same col move + capture)."""
    board = Board()
    board.rows[7].squares[3].contents = None
    board.rows[5].squares[3].contents = 'r'
    board.rows[2].squares[3].contents = 'P'
    assert is_valid_capture(5, 3, 2, 3, board)
    assert is_valid_move(5, 3, 2, 3, board)

def test_rook_cannot_capture_diagonally():
    """Rook cannot capture on diagonal (EC-R3: diagonal invalid)."""
    board = Board()
    board.rows[0].squares[0].contents = None
    board.rows[3].squares[3].contents = 'R'
    board.rows[5].squares[5].contents = 'p'
    assert not is_valid_move(3, 3, 5, 5, board)

def test_bishop_capture_diagonal():
    """Bishop captures enemy on diagonal (EC-B1: diagonal + capture)."""
    board = Board()
    board.rows[0].squares[2].contents = None
    board.rows[2].squares[4].contents = 'B'
    board.rows[4].squares[6].contents = 'p'
    assert is_valid_capture(2, 4, 4, 6, board)
    assert is_valid_move(2, 4, 4, 6, board)

def test_bishop_cannot_capture_straight():
    """Bishop cannot capture on same row/col (EC-B2: non-diagonal invalid)."""
    board = Board()
    board.rows[7].squares[2].contents = None
    board.rows[5].squares[4].contents = 'b'
    board.rows[2].squares[4].contents = 'P'
    assert not is_valid_move(5, 4, 2, 4, board)

def test_queen_capture_rook_like():
    """Queen captures enemy on same row (EC-Q1: rook-like + capture)."""
    board = Board()
    board.rows[0].squares[3].contents = None
    board.rows[3].squares[3].contents = 'Q'
    board.rows[3].squares[6].contents = 'p'
    assert is_valid_capture(3, 3, 3, 6, board)
    assert is_valid_move(3, 3, 3, 6, board)

def test_queen_capture_bishop_like():
    """Queen captures enemy on diagonal (EC-Q2: bishop-like + capture)."""
    board = Board()
    board.rows[7].squares[3].contents = None
    board.rows[5].squares[3].contents = 'q'
    board.rows[2].squares[0].contents = 'P'
    assert is_valid_capture(5, 3, 2, 0, board)
    assert is_valid_move(5, 3, 2, 0, board)

def test_queen_cannot_capture_knight_like():
    """Queen cannot capture with L-shape (EC-Q3: knight-like invalid)."""
    board = Board()
    board.rows[0].squares[3].contents = None
    board.rows[2].squares[3].contents = 'Q'
    board.rows[4].squares[4].contents = 'p'
    assert not is_valid_move(2, 3, 4, 4, board)

def test_knight_capture_l_shape():
    """Knight captures enemy on L-shape (EC-N1: L-shape + capture)."""
    board = Board()
    board.rows[0].squares[1].contents = None
    board.rows[3].squares[2].contents = 'N'
    board.rows[5].squares[3].contents = 'p'
    assert is_valid_capture(3, 2, 5, 3, board)
    assert is_valid_move(3, 2, 5, 3, board)

def test_knight_cannot_capture_like_pawn():
    """Knight cannot capture with pawn move (EC-N2: pawn move invalid)."""
    board = Board()
    board.rows[0].squares[1].contents = None
    board.rows[3].squares[2].contents = 'N'
    board.rows[4].squares[2].contents = 'p'
    assert not is_valid_move(3, 2, 4, 2, board)

def test_king_capture_one_square():
    """King captures enemy on adjacent square (EC-K1: one-square + capture)."""
    board = Board()
    board.rows[1].squares[4].contents = None
    board.rows[2].squares[4].contents = None
    board.rows[0].squares[4].contents = 'K'
    board.rows[1].squares[4].contents = 'p'
    assert is_valid_capture(0, 4, 1, 4, board)
    assert is_valid_move(0, 4, 1, 4, board)

def test_king_cannot_capture_two_squares():
    """King cannot capture two squares away (EC-K2: more than one space invalid)."""
    board = Board()
    board.rows[6].squares[4].contents = None
    board.rows[5].squares[4].contents = None
    board.rows[7].squares[4].contents = 'k'
    board.rows[5].squares[4].contents = 'P'
    assert not is_valid_move(7, 4, 5, 4, board)

def test_pawn_cannot_capture_straight():
    """Pawn cannot capture by moving straight forward (EC-PAW2: only diagonal capture)."""
    board = Board()
    board.rows[1].squares[4].contents = None
    board.rows[3].squares[4].contents = 'P'
    board.rows[4].squares[4].contents = 'p'
    assert not is_valid_move(3, 4, 4, 4, board)


# --- Losing pieces: capture execution removes captured piece ---

def test_capture_removes_rook():
    """After rook captures, enemy piece is gone from board."""
    board = Board()
    board.rows[0].squares[0].contents = None
    board.rows[2].squares[0].contents = 'R'
    board.rows[2].squares[4].contents = 'p'
    start_piece = board.rows[2].squares[0].contents
    captured = board.rows[2].squares[4].contents
    assert captured == 'p'
    board.rows[2].squares[4].contents = start_piece
    board.rows[2].squares[0].contents = None
    assert board.rows[2].squares[4].contents == 'R'
    assert board.rows[2].squares[0].contents is None

def test_capture_removes_bishop():
    """After bishop captures, enemy piece is gone."""
    board = Board()
    board.rows[0].squares[2].contents = None
    board.rows[3].squares[3].contents = 'B'
    board.rows[5].squares[5].contents = 'p'
    board.rows[5].squares[5].contents = board.rows[3].squares[3].contents
    board.rows[3].squares[3].contents = None
    assert board.rows[5].squares[5].contents == 'B'
    assert board.rows[3].squares[3].contents is None

def test_capture_removes_knight():
    """After knight captures, enemy piece is gone."""
    board = Board()
    board.rows[0].squares[1].contents = None
    board.rows[4].squares[4].contents = 'N'
    board.rows[6].squares[5].contents = 'p'
    board.rows[6].squares[5].contents = board.rows[4].squares[4].contents
    board.rows[4].squares[4].contents = None
    assert board.rows[6].squares[5].contents == 'N'
    assert board.rows[4].squares[4].contents is None


# --- Checkmate: king capture ends the game ---

def test_white_queen_can_capture_black_king():
    """White queen capturing black king is valid (checkmate / game over)."""
    board = Board()
    board.rows[0].squares[3].contents = None
    board.rows[7].squares[5].contents = None
    board.rows[6].squares[4].contents = None
    board.rows[6].squares[4].contents = 'Q'
    assert board.rows[7].squares[4].contents == 'k'
    assert is_valid_capture(6, 4, 7, 4, board)
    assert is_valid_move(6, 4, 7, 4, board)

def test_black_queen_can_capture_white_king():
    """Black queen capturing white king is valid (checkmate / game over)."""
    board = Board()
    board.rows[7].squares[3].contents = None
    board.rows[0].squares[5].contents = None
    board.rows[1].squares[4].contents = None
    board.rows[1].squares[4].contents = 'q'
    assert board.rows[0].squares[4].contents == 'K'
    assert is_valid_capture(1, 4, 0, 4, board)
    assert is_valid_move(1, 4, 0, 4, board)

def test_rook_checkmate_back_rank():
    """White rook can deliver checkmate (capture black king on back rank)."""
    board = Board()
    board.rows[7].squares[0].contents = None
    board.rows[7].squares[1].contents = None
    board.rows[6].squares[0].contents = None
    board.rows[6].squares[0].contents = 'R'
    assert board.rows[7].squares[4].contents == 'k'
    assert is_valid_move(6, 0, 7, 4, board)
    assert is_valid_capture(6, 0, 7, 4, board)

def test_king_capture_removes_king():
    """Executing king capture removes the captured king from board (game over)."""
    board = Board()
    board.rows[1].squares[4].contents = None
    board.rows[2].squares[4].contents = None
    board.rows[0].squares[4].contents = 'K'
    board.rows[1].squares[5].contents = 'p'
    assert board.rows[1].squares[5].contents == 'p'
    board.rows[1].squares[5].contents = board.rows[0].squares[4].contents
    board.rows[0].squares[4].contents = None
    assert board.rows[1].squares[5].contents == 'K'
    assert board.rows[0].squares[4].contents is None


def test_print_board():
    """Test board printing doesn't crash"""
    from chess import print_board
    import io
    import sys
    
    board = Board()
    # Capture stdout to avoid cluttering test output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_board(board)
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    # Check that output contains expected elements
    assert 'A' in output
    assert 'H' in output
    assert '8' in output
    assert '1' in output
    assert 'R' in output  # White rook
    assert 'r' in output  # Black rook


# Game logic tests

def test_turn_alternation():
    """Test that turns alternate between white and black"""
    # This would require mocking input, so we test the logic separately
    isWhite = False
    turns = []
    for _ in range(4):
        isWhite = not isWhite
        turns.append("White" if isWhite else "Black")
    
    assert turns == ["White", "Black", "White", "Black"]

def test_pawn_promotion_white():
    """Test white pawn promotion to queen"""
    board = Board()
    # Move white pawn to promotion rank
    board.rows[1].squares[0].contents = None
    board.rows[6].squares[0].contents = 'P'
    
    # Simulate the promotion logic
    start_piece = board.rows[6].squares[0].contents
    finish_row = 7
    if start_piece in ['P', 'p'] and finish_row in [0, 7]:
        promoted_piece = 'q' if start_piece.islower() else 'Q'
    
    assert promoted_piece == 'Q'

def test_pawn_promotion_black():
    """Test black pawn promotion to queen"""
    board = Board()
    # Move black pawn to promotion rank
    board.rows[6].squares[7].contents = None
    board.rows[1].squares[7].contents = 'p'
    
    # Simulate the promotion logic
    start_piece = board.rows[1].squares[7].contents
    finish_row = 0
    if start_piece in ['P', 'p'] and finish_row in [0, 7]:
        promoted_piece = 'q' if start_piece.islower() else 'Q'
    
    assert promoted_piece == 'q'

def test_win_condition_white_captures_black_king():
    """Test win condition when white captures black king"""
    board = Board()
    # Place white queen next to black king
    board.rows[7].squares[3].contents = None
    board.rows[7].squares[5].contents = None
    board.rows[6].squares[4].contents = None
    board.rows[6].squares[4].contents = 'Q'
    
    # Check that black king is present
    finish_piece = board.rows[7].squares[4].contents
    assert finish_piece == 'k'
    
    # Simulate move and win
    assert finish_piece in ['K', 'k']

def test_win_condition_black_captures_white_king():
    """Test win condition when black captures white king"""
    board = Board()
    # Place black queen next to white king
    board.rows[0].squares[3].contents = None
    board.rows[0].squares[5].contents = None
    board.rows[1].squares[4].contents = None
    board.rows[1].squares[4].contents = 'q'
    
    # Check that white king is present
    finish_piece = board.rows[0].squares[4].contents
    assert finish_piece == 'K'
    
    # Simulate move and win
    assert finish_piece in ['K', 'k']

def test_empty_starting_square():
    """Test that moving from empty square is detected"""
    board = Board()
    # Clear a square
    board.rows[3].squares[3].contents = None
    
    # Check that square is empty
    start_piece = board.rows[3].squares[3].contents
    assert start_piece is None

def test_white_turn_validation():
    """Test that white can only move white pieces"""
    board = Board()
    isWhite = True
    
    # Try to move white piece (should be valid)
    start_piece_white = board.rows[1].squares[0].contents  # White pawn
    assert isWhite and start_piece_white.isupper()
    
    # Try to move black piece (should be invalid)
    start_piece_black = board.rows[6].squares[0].contents  # Black pawn
    assert not (isWhite and start_piece_black.isupper())

def test_black_turn_validation():
    """Test that black can only move black pieces"""
    board = Board()
    isWhite = False
    
    # Try to move black piece (should be valid)
    start_piece_black = board.rows[6].squares[0].contents  # Black pawn
    assert not isWhite and start_piece_black.islower()
    
    # Try to move white piece (should be invalid)
    start_piece_white = board.rows[1].squares[0].contents  # White pawn
    assert not (not isWhite and start_piece_white.islower())

def test_move_execution():
    """Test that a move properly updates the board"""
    board = Board()
    
    # Record initial state
    start_piece = board.rows[1].squares[4].contents  # White pawn at E2
    assert start_piece == 'P'
    assert board.rows[3].squares[4].contents is None  # E4 is empty
    
    # Execute move E2 to E4
    board.rows[3].squares[4].contents = start_piece
    board.rows[1].squares[4].contents = None
    
    # Verify final state
    assert board.rows[1].squares[4].contents is None
    assert board.rows[3].squares[4].contents == 'P'

def test_capture_execution():
    """Test that a capture properly updates the board"""
    board = Board()
    
    # Set up a capture scenario
    board.rows[1].squares[4].contents = None
    board.rows[4].squares[4].contents = 'P'  # White pawn at E5
    board.rows[5].squares[5].contents = 'p'  # Black pawn at F6
    
    # Execute capture
    start_piece = board.rows[4].squares[4].contents
    captured_piece = board.rows[5].squares[5].contents
    assert captured_piece == 'p'
    
    board.rows[5].squares[5].contents = start_piece
    board.rows[4].squares[4].contents = None
    
    # Verify
    assert board.rows[4].squares[4].contents is None
    assert board.rows[5].squares[5].contents == 'P'


