import heapq

class Solution:
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # dist[t][i][j] = min cost
        dist = [[[INF]*n for _ in range(m)] for _ in range(k+1)]
        dist[0][0][0] = 0

        # All cells sorted by value
        cells = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))

        pq = [(0, 0, 0, 0)]  # (cost, i, j, teleports_used)

        # For each teleport count, pointer into sorted cells
        ptr = [0] * (k+1)

        while pq:
            cost, i, j, t = heapq.heappop(pq)
            if cost != dist[t][i][j]:
                continue

            # Reached destination
            if i == m-1 and j == n-1:
                return cost

            # Normal moves
            if i + 1 < m:
                nc = cost + grid[i+1][j]
                if nc < dist[t][i+1][j]:
                    dist[t][i+1][j] = nc
                    heapq.heappush(pq, (nc, i+1, j, t))

            if j + 1 < n:
                nc = cost + grid[i][j+1]
                if nc < dist[t][i][j+1]:
                    dist[t][i][j+1] = nc
                    heapq.heappush(pq, (nc, i, j+1, t))

            # Teleport moves
            if t < k:
                while ptr[t] < len(cells) and cells[ptr[t]][0] <= grid[i][j]:
                    _, x, y = cells[ptr[t]]
                    if cost < dist[t+1][x][y]:
                        dist[t+1][x][y] = cost
                        heapq.heappush(pq, (cost, x, y, t+1))
                    ptr[t] += 1

        return -1
