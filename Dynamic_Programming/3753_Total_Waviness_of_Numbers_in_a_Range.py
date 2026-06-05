from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, length, prev2, prev1):
                if pos == m:
                    return (1, 0)  # (count, total_waviness)

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            0,
                            10,
                            10
                        )
                        total_cnt += cnt
                        total_wav += wav

                    else:
                        if length == 0:
                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                1,
                                10,
                                d
                            )

                        elif length == 1:
                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                2,
                                prev1,
                                d
                            )

                        else:
                            add = 1 if (
                                (prev1 > prev2 and prev1 > d) or
                                (prev1 < prev2 and prev1 < d)
                            ) else 0

                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                2,
                                prev1,
                                d
                            )

                            wav += add * cnt

                        total_cnt += cnt
                        total_wav += wav

                return total_cnt, total_wav

            return dp(0, True, False, 0, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)
