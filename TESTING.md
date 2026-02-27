## Installation

First, install pytest if you haven't already:

```bash
pip install pytest
```

## Running Tests

### Run all tests
```bash
pytest test_chess.py
```

### Run tests with verbose output
```bash
pytest test_chess.py -v
```

### Run a specific test function
```bash
pytest test_chess.py::test_pawn_wp1
```

### Run all tests in a category (e.g., all pawn tests)
```bash
pytest test_chess.py -k "pawn"
```

### Run tests and show print output
```bash
pytest test_chess.py -s
```

## Test Coverage

The test suite includes comprehensive tests for:

- **Distance tests** - Validate move distance rules
- **Path tests** - Ensure pieces cannot move through obstructions
- **Pawn tests** - Forward movement, two-square initial move, diagonal captures, and promotion
- **Rook tests** - Horizontal and vertical movement
- **Bishop tests** - Diagonal movement
- **Queen tests** - Combined rook and bishop movement patterns
- **Knight tests** - L-shaped movement patterns
- **King tests** - Single square movement in any direction
- **Boundary tests** - Edge cases and full board traversal

## Understanding Test Cases

Each test is named with a pattern: `test_<piece>_<id>`

For example:
- `test_pawn_wp1` - White Pawn test case 1
- `test_bishop_b2` - Bishop test case 2
- `test_boundary_bv3` - Boundary test case 3

## Board Coordinate System

Tests use a 0-indexed coordinate system:

**Column mapping (letters to numbers):**
- A = 0, B = 1, C = 2, D = 3, E = 4, F = 5, G = 6, H = 7

**Row mapping:**
- Row 1 = 0, Row 2 = 1, ..., Row 8 = 7

**Example:** To reference square A2:
```python
board.rows[1].squares[0]  # Row 2 (index 1), Column A (index 0)
```

**Testing a move from A2 to A4:**
```python
is_valid_move(1, 0, 3, 0, board)  # from row 2, col A to row 4, col A
```
