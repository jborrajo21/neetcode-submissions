class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def bt(start):
            if start == len(nums):
                perms.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                bt(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
            return
        
        bt(0)
        return perms