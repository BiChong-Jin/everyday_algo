class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        rows, cols = len(mat), len(mat[0])
        res = []

        for d in range(cols + rows - 1):
            curr = []

            head_row, head_col = 0 if d < cols else d - cols + 1, (
                d if d < cols else cols - 1
            )

            while head_row < rows and head_col > -1:
                curr.append(mat[head_row][head_col])
                head_row += 1
                head_col -= 1

            if not d % 2:
                res.extend(curr[::-1])

            else:
                res.extend(curr)

        return res
