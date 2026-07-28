class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        nums.sort()
        def bt(state, total, start):
            if total == target:
                combs.append(state.copy())
            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    break
                state.append(nums[i])
                bt(state, total + nums[i], i)
                state.pop()
            return
        
        bt([], 0, 0)
        return combs