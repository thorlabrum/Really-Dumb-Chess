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



