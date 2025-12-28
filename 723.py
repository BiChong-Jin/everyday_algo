class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows, cols = len(board), len(board[0])

        def find():
            crushed_set = set()
            # check vertical
            for r in range(1, rows - 1):
                for c in range(cols):
                    if board[r][c] == 0:
                        continue

                    if board[r][c] == board[r - 1][c] == board[r + 1][c]:
                        crushed_set.add((r, c))
                        crushed_set.add((r + 1, c))
                        crushed_set.add((r - 1, c))

            # check horizontal
            for r in range(rows):
                for c in range(1, cols - 1):
                    if board[r][c] == 0:
                        continue

                    if board[r][c] == board[r][c - 1] == board[r][c + 1]:
                        crushed_set.add((r, c))
                        crushed_set.add((r, c + 1))
                        crushed_set.add((r, c - 1))

            return crushed_set

        def crush(crushed_set):
            for row, col in crushed_set:
                board[row][col] = 0

        def drop():
            for c in range(cols):
                lowest_zero = -1

                for r in range(rows - 1, -1, -1):
                    if board[r][c] == 0:
                        lowest_zero = max(r, lowest_zero)

                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = (
                            board[lowest_zero][c],
                            board[r][c],
                        )
                        lowest_zero -= 1

        crushed_set = find()

        while crushed_set:
            crush(crushed_set)
            drop()
            crushed_set = find()

        return board
