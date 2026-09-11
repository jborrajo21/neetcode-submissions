class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        jumps = 0
        while r < len(nums) - 1:
            nr = nums[l]
            for i in range(l, r + 1):
                nr = max(nr, i + nums[i])
            l = r + 1
            r = nr
            jumps+=1



        return jumps