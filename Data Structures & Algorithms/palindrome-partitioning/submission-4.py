class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pals = []
        def bt(start, state):
            if start == len(s):
                pals.append(state.copy())
                return
            for i in range(start, len(s)):
                if s[start: i + 1] == s[start: i + 1][::-1]:
                    state.append(s[start: i + 1])
                    bt(i + 1, state)
                    state.pop()
            return 
        
        bt(0, [])
        return pals