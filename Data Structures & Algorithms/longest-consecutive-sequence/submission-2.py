class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_length = 0
        for i in range(len(nums)):
            num = nums[i]
            if num - 1 in numSet: continue
            length = 1
            while num + 1 in numSet:
                length += 1 
                num += 1
            max_length = max(max_length, length)
        return max_length

