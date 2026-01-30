class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        INF = 10**18

        # Group rules by length
        from collections import defaultdict
        rules = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            rules[len(o)].append((o, c, w))

        # For each length, build Floyd–Warshall graph
        dist = {}  # length -> { (s,t): min cost }

        for L, lst in rules.items():
            strs = set()
            for o, c, _ in lst:
                strs.add(o)
                strs.add(c)
            strs = list(strs)
            idx = {s: i for i, s in enumerate(strs)}
            m = len(strs)

            d = [[INF]*m for _ in range(m)]
            for i in range(m):
                d[i][i] = 0

            for o, c, w in lst:
                d[idx[o]][idx[c]] = min(d[idx[o]][idx[c]], w)

            for k in range(m):
                for i in range(m):
                    for j in range(m):
                        if d[i][k] + d[k][j] < d[i][j]:
                            d[i][j] = d[i][k] + d[k][j]

            dist[L] = (d, idx)

        # DP
        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            # Single character (no cost)
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            # Substring replacements
            for L, (d, idx) in dist.items():
                if i + L <= n:
                    s = source[i:i+L]
                    t = target[i:i+L]
                    if s in idx and t in idx:
                        c = d[idx[s]][idx[t]]
                        if c < INF:
                            dp[i] = min(dp[i], c + dp[i + L])

        return dp[0] if dp[0] < INF else -1
