class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                l = j - i + 1
                if s[i] == s[j] and (l <=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        
        return count