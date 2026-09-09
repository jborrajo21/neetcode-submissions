class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r,count=0,0,0
        while r < len(nums) - 1:
            nr = l
            for i in range(l, r+1):
                nr = max(nr, i + nums[i])
            count+=1
            l = r+1
            r = nr
        
        return count
