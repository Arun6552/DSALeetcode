class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        # Prefix sums
        row_ps = [[0] * (n + 1) for _ in range(m)]
        col_ps = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_ps[i][j + 1] = row_ps[i][j] + grid[i][j]
                col_ps[i + 1][j] = col_ps[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        def row_sum(r, c1, c2):
            return row_ps[r][c2] - row_ps[r][c1]

        def col_sum(c, r1, r2):
            return col_ps[r2][c] - col_ps[r1][c]

        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    target = row_sum(r, c, c + k)

                    # Check rows
                    if any(row_sum(r + i, c, c + k) != target for i in range(k)):
                        continue

                    # Check columns
                    if any(col_sum(c + j, r, r + k) != target for j in range(k)):
                        continue

                    # Check diagonals
                    if diag1[r + k][c + k] - diag1[r][c] != target:
                        continue
                    if diag2[r + k][c] - diag2[r][c + k] != target:
                        continue

                    return k

        return 1
