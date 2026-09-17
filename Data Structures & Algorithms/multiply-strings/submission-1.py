class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                res[i + j + 1] += int(num1[i]) * int(num2[j])
        
        for k in range(m + n - 1, 0, -1):
            res[k - 1] += res[k] // 10
            res[k] %= 10
        
        return "".join(map(str, res)).lstrip("0")