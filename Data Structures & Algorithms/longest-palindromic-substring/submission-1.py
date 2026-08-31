class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]
    
        resIdx, resLen = 0,1

        for i in range(n-1,-1,-1):
            for j in range(i, n):
                l = j-i+1
                if (l <= 2 or dp[i+1][j-1])and s[i] == s[j]:
                    dp[i][j] = True
                    if l > resLen:
                        resLen = l
                        resIdx = i
         
        return s[resIdx: resIdx + resLen]