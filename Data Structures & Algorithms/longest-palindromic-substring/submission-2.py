class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        resLen = 0
        resIdx = -1

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                l = j - i + 1
                if (l <=2 or dp[i+1][j-1]) and s[i] == s[j]:
                    dp[i][j] = True
                    if resLen < l:
                        resLen = l
                        resIdx = i
        
        return s[resIdx: resIdx + resLen]

