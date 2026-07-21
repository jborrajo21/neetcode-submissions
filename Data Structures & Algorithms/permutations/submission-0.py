class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def backtrack(state, actions):
            if not actions:
                perms.append(state.copy())
                return
            for action in actions:
                state.append(action)
                new = actions.copy()
                new.remove(action)
                backtrack(state, new)
                state.pop()
            return

        backtrack([], set(nums))
        return perms