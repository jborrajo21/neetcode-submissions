class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = []
        for i in range(len(num2) -1,-1,-1):
            num = 0
            for j in range(len(num1)-1,-1,-1):
                num += (int(num2[i]) * int(num1[j])) * (10 ** (len(num1) - 1 - j))
            nums.append(num * (10 **(len(num2) - 1 - i)))


        return str(sum(nums))