class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def bt(state, start):
            subsets.append(state.copy())
            for i in range(start, len(nums)):
                state.append(nums[i])
                bt(state, i + 1)
                state.pop()
            return
        bt([], 0)
        return subsets