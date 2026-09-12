class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0
        r = 0
        while r < len(nums) - 1:
            nr = -1
            for i in range(l, r+1):
                nr = max(nr, nums[i] + i)
            l = r+1
            r = nr
            jumps+=1
        
        return jumps