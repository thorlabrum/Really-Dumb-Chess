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

def test_distance():
    print('----------------Distance tests----------------')
    #TC-D1
    board = Board()
    valid = is_valid_move(1, 4, 1, 4, board)
    assert not valid
    print(f'TC-D1:\nExpected: False\nResult {valid}\n')
    
    # TC-D2
    board = Board()
    # Arranging board for TC-D2
    # Removing pieces in path
    board.rows[1].squares[0].contents = None
    board.rows[6].squares[0].contents = None
    
    valid = is_valid_move(0, 0, 7, 0, board)
    assert valid
    print(f'TC-D2:\nExpected: True\nResult {valid}\n')

    # TC-D3
    board = Board()
    valid = is_valid_move(1, 6, 3, 6, board)
    assert valid
    print(f'TC-D3:\nExpected: True\nResult {valid}\n')



def test_path():
    print('----------------Pathing test----------------')

    # TC-P1
    board = Board()
    valid = is_valid_move(0, 3, 3, 0, board)
    assert not valid
    print(f'TC-P1:\nExpected: False\nResult {valid}\n')



def test_pawns():
    print('----------------Pawn tests----------------')
    
    # TC-WP1
    board = Board()
    valid = is_valid_move(1, 7, 2, 7, board)
    assert valid
    print(f'TC-WP1:\nExpected: True\nResult {valid}\n')

    # TC-BP1
    board = Board()
    valid = is_valid_move(6, 1, 5, 1, board)
    assert valid
    print(f'TC-BP1:\nExpected: True\nResult {valid}\n')

    # TC-BP2
    board = Board()
    valid = is_valid_move(6, 1, 4, 1, board)
    assert valid
    print(f'TC-BP2:\nExpected: True\nResult {valid}\n')

    # TC-PAW1
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
    print(f'TC-PAW1:\nExpected: True\nResult {valid}\n')

    # TC-PAW2
    board = Board()
    # Arranging board for TC-PAW2
    # Black pawn move
    board.rows[6].squares[4].contents = None
    board.rows[4].squares[4].contents = 'p'

    valid = is_valid_move(4, 4, 5, 4, board)
    assert not valid
    print(f'TC-PAW2:\nExpected: False\nResult {valid}\n')



def test_rooks():
    print('----------------Rook tests----------------')

    # TC-R1
    board = Board()
    # Arranging board for TC-R1
    # Moving black rook
    board.rows[7].squares[0].contents = None
    board.rows[2].squares[0].contents = 'r'

    valid = is_valid_move(2, 0, 2, 7, board)
    assert valid
    print(f'TC-R1:\nExpected: True\nResult {valid}\n')

    # TC-R2
    board = Board()
    # Arranging board for TC-R2
    # Moving white rook
    board.rows[0].squares[0].contents = None
    board.rows[2].squares[0].contents = 'R'

    valid = is_valid_move(2, 0, 4, 1, board)
    assert not valid
    print(f'TC-R2:\nExpected: False\nResult {valid}\n')



def test_bishops():
    print('----------------Bishop tests----------------')

    # TC-B1
    board = Board()
    # Arranging board for TC-B1
    # Moving white bishop
    board.rows[0].squares[2].contents = None
    board.rows[2].squares[4].contents = 'B'

    valid = is_valid_move(2, 4, 3, 3, board)
    assert valid
    print(f'TC-B1:\nExpected: True\nResult {valid}\n')

    # TC-B2
    board = Board()
    # Arranging board for TC-B2
    # Moving black bisop
    board.rows[7].squares[2].contents = None
    board.rows[5].squares[4].contents = 'b'

    valid = is_valid_move(5, 4, 5, 0, board)
    assert not valid
    print(f'TC-B2:\nExpected: False\nResult {valid}\n')

    # TC-B3
    board = Board()
    valid = is_valid_move(0, 5, 2, 3, board)
    assert not valid
    print(f'TC-B3:\nExpected: False\nResult {valid}\n')



def test_queens():
    print('----------------Queen tests----------------')

    # TC-Q1
    board = Board()
    # Arranging board for TC-Q1
    # Moving white queen
    board.rows[0].squares[3].contents = None
    board.rows[2].squares[3].contents = 'Q'

    valid = is_valid_move(2, 3, 2, 0, board)
    assert valid
    print(f'TC-Q1:\nExpected: True\nResult {valid}\n')

    # TC-Q2
    board = Board()
    # Arranging board for TC-Q2
    # Moving black queen
    board.rows[7].squares[3].contents = None
    board.rows[5].squares[3].contents = 'q'

    valid = is_valid_move(5, 3, 3, 5, board)
    assert valid
    print(f'TC-Q2:\nExpected: True\nResult {valid}\n')

    # TC-Q3
    board = Board()
    valid = is_valid_move(0, 3, 2, 4, board)
    assert not valid
    print(f'TC-Q3:\nExpected: False\nResult {valid}\n')

    # TC-Q4
    board = Board()
    valid = is_valid_move(0, 3, 2, 3, board)
    assert not valid
    print(f'TC-Q4:\nExpected: False\nResult {valid}\n')

    # TC-Q5
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
    print(f'TC-Q5:\nExpected: False\nResult {valid}\n')



def test_knights():
    print('----------------Knight tests----------------')


    # TC-N1
    board = Board()
    # Arranging board for TC-N1
    # Moving white knight
    board.rows[0].squares[1].contents = None
    board.rows[2].squares[2].contents = 'N'

    valid = is_valid_move(2, 2, 3, 4, board)
    assert valid
    print(f'TC-N1:\nExpected: True\nResult {valid}\n')

    # TC-N2
    board = Board()
    valid = is_valid_move(7, 6, 5, 5, board)
    assert valid
    print(f'TC-N2:\nExpected: True\nResult {valid}\n')

    # TC-N3
    board = Board()
    # Arranging board for TC-N3
    # Moving black knight
    board.rows[0].squares[6].contents = None
    board.rows[2].squares[5].contents = 'N'

    valid = is_valid_move(2, 5, 6, 5, board)
    assert not valid
    print(f'TC-N3:\nExpected: False\nResult {valid}\n')



def test_kings():
    print('----------------King tests----------------')


    # TC-K1
    board = Board()
    # Arranging board for TC-K1
    # Moving white pawn
    board.rows[1].squares[4].contents = None
    board.rows[2].squares[4].contents = 'P'

    valid = is_valid_move(0, 4, 1, 4, board)
    assert valid
    print(f'TC-K1:\nExpected: True\nResult {valid}\n')

    # TC-K2
    board = Board()
    # Arranging board for TC-K2
    # Removing piece in path
    board.rows[6].squares[4].contents = None
 
    valid = is_valid_move(7, 4, 3, 4, board)
    assert not valid
    print(f'TC-K2:\nExpected: False\nResult {valid}\n')



def test_boundaries():
    print('----------------Boundary tests----------------')


    # TC-BV1
    board = Board()
    # Arranging board for TC-BV1
    # Removing all pieces from B1 to H1
    for i in range(1, 8):
        board.rows[0].squares[i].contents = None

    valid = is_valid_move(0, 0, 0, 7, board)
    assert valid
    print(f'TC-BV1:\nExpected: True\nResult {valid}\n')

    # TC-BV2
    board = Board()
    # Arranging board for TC-BV2
    # Removing pawn in path
    board.rows[6].squares[0].contents = None
    # Moving black king
    board.rows[7].squares[4].contents = None
    board.rows[7].squares[0].contents = 'k'

    valid = is_valid_move(7, 0, 5, 0, board)
    assert not valid
    print(f'TC-BV2:\nExpected: False\nResult {valid}\n')

    # TC-BV3
    board = Board()
    # Arranging board for TC-BV3
    # Removing pawn in path
    board.rows[1].squares[3].contents = None

    valid = is_valid_move(0, 2, 5, 7, board)
    assert valid
    print(f'TC-BV3:\nExpected: True\nResult {valid}\n')

    # TC-BV4
    board = Board()
    # Arranging board for TC-BV4
    # Removing pieces in path
    board.rows[1].squares[3].contents = None
    board.rows[6].squares[3].contents = None
    board.rows[7].squares[3].contents = None


    valid = is_valid_move(0, 3, 7, 3, board)
    assert valid
    print(f'TC-BV4:\nExpected: True\nResult {valid}\n')



def run_tests():
    test_distance()
    test_path()
    test_pawns()
    test_rooks()
    test_bishops()
    test_queens()
    test_knights()
    test_kings()
    test_boundaries()


if __name__ == "__main__":
    run_tests()
