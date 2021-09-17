import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        dp = [True]*n
        dp[0] = dp[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = False
        return sum(dp)