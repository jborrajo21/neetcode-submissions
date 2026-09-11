class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        dp = [[False] * (m+1) for _ in range(n+1)]

        dp[n][m] = True

        for i in range(n-1,-1,-1):
            dp[i][m] = s1[i] == s3[i+m]
            if not dp[i][m]:
                break
        
        for j in range(m-1,-1,-1):
            dp[n][j] = s2[j] == s3[j+n]
            if not dp[n][j]:
                break
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                dp[i][j] = (s1[i] == s3[i+j] and dp[i+1][j]) or (s2[j] == s3[i+j] and dp[i][j+1])
        
        return dp[0][0]