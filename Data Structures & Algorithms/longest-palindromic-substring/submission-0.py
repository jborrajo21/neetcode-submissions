class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                l = j - i + 1
                if s[i] == s[j] and (l <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if l > resLen:
                        resLen = l
                        resIdx = i
        
        return s[resIdx:resIdx + resLen]
                    