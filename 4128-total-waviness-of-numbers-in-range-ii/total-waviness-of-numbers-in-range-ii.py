from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n < 0:
                return 0

            s = str(n)

            @cache
            def dp(pos, tight, started, prev2, prev1):
                if pos == len(s):
                    return (1, 0)  # (count, waviness)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, ntight, False, -1, -1)

                    elif not started:
                        cnt, wav = dp(pos + 1, ntight, True, -1, d)

                    elif prev2 == -1:
                        cnt, wav = dp(pos + 1, ntight, True, prev1, d)

                    else:
                        add = int(
                            (prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)
                        )

                        cnt, wav = dp(pos + 1, ntight, True, prev1, d)
                        wav += add * cnt

                    total_cnt += cnt
                    total_wavy += wav

                return total_cnt, total_wavy

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)