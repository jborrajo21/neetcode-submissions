class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False
        if not s2:
            return s1 == s3
        if not s1:
            return s2 == s3

        dp = [[False] * (m+1) for _ in range(n+1)]
        
        dp[n][m] = True
        
        for i in range(n-1, -1, -1):
            dp[i][m] = dp[i+1][m] and (s1[i] == s3[m+i])
        for j in range(m-1, -1, -1):
            dp[n][j] = dp[n][j+1] and (s2[j] == s3[n+j])

        print(dp)

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                dp[i][j] = (s1[i] == s3[i+j] and dp[i+1][j]) or (s2[j] == s3[i+j] and dp[i][j+1])
        
        return dp[0][0]

    