class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = len(nums) - 1
        for i in range(len(nums) -2,-1,-1):
            if nums[i] + i >= curr:
                curr = i
        return curr == 0
