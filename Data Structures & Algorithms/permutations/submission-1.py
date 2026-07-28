class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def bt(state, start):
            if start == len(nums):
                perms.append(state.copy())
                return
            for i in range(start, len(nums)):
                state[start], state[i] = state[i], state[start]
                bt(state, start + 1)
                state[start], state[i] = state[i], state[start]
            return
        
        bt(nums, 0)
        return perms
            