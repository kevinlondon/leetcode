import pytest


def sudoku_solve(board):
    """
    Ideas:
    * Each subboard must contain all numbers
    * Each row and column must contain all numbers
    * Could track what options are available for a given slot by comparing the options for the row, column, grid.

    Column[0]: Have: {4, 5, 6, 7, 8}, Need: {1, 2, 3, 9}
    Column[1]: Have: {3, 6, 9}, Need: {1, 2, 4, 5, 7, 8}
    Column[2]: {1, 2, 3, 4, 5, 6, 7, 9}
    . . .

    Row[0]: Need: {1,2, 4, 6, 8, 9}
    Row[1]: Need: {2, 3, 4, 7, 8}
    Row[2]: Need: {1, 2, 3, 4, 5, 7}

    Box[0]: Need: {1, 2, 4, 7}

    Box[0] & Row[2] & Column[0] = Need: {1, 2}
    Box[0] & Row[1] & Column[1] = Need: {2, 4, 7}
    Box[0] & Row[0] & Column[2] = {1, 2, 4}
    B[0] & R[1] & C[2] = {2, 4, 7}
    """

    candidates = None
    row = None
    col = None

    for y in range(9):
        for x in range(9):
            if board[y][x] == ".":
                new_candidates = get_candidates(board, x, y)
                if not new_candidates:
                    return False

                if not candidates or len(new_candidates) < len(candidates):
                    candidates = new_candidates
                    row = y
                    col = x

    if candidates is None:
        return True

    for val in candidates:
        board[row][col] = val
        if sudoku_solve(board):
            return True

        board[row][col] = "."

    return False


def get_candidates(board, x, y):
    candidates = []

    for num in range(1, 10):
        num = str(num)
        collision = False
        for i in range(9):
            bx = (x - x % 3) + i % 3
            by = (y - y % 3) + i // 3
            if num in (board[y][i], board[i][x], board[by][bx]):
                collision = True
                break

        if not collision:
            candidates.append(num)

    return candidates


tc1 = [
    [".", ".", ".", "7", ".", ".", "3", ".", "1"],
    ["3", ".", ".", "9", ".", ".", ".", ".", "."],
    [".", "4", ".", "3", "1", ".", "2", ".", "."],
    [".", "6", ".", "4", ".", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "1", ".", ".", "8", ".", "4", "."],
    [".", ".", "6", ".", "2", "1", ".", "5", "."],
    [".", ".", ".", ".", ".", "9", ".", ".", "8"],
    ["8", ".", "5", ".", ".", "4", ".", ".", "."],
]


tc2 = [
    [".", "8", "9", ".", "4", ".", "6", ".", "5"],
    [".", "7", ".", ".", ".", "8", ".", "4", "1"],
    ["5", "6", ".", "9", ".", ".", ".", ".", "8"],
    [".", ".", ".", "7", ".", "5", ".", "9", "."],
    [".", "9", ".", "4", ".", "1", ".", "5", "."],
    [".", "3", ".", "9", ".", "6", ".", "1", "."],
    ["8", ".", ".", ".", ".", ".", ".", ".", "7"],
    [".", "2", ".", "8", ".", ".", ".", "6", "."],
    [".", ".", "6", ".", "7", ".", ".", "8", "."],
]

tc3 = [
    [".", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["1", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]


@pytest.mark.parametrize("board,expected", [(tc1, True), (tc2, False), (tc3, False)])
def test_examples(board, expected):
    assert sudoku_solve(board) is expected
