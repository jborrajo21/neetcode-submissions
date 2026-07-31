class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        
        def bt(state, start):
            if start == len(s):
                palindromes.append(state.copy())
                return
            state.append(s[start])
            bt(state, start + 1)
            state.pop()
            for j in range(start + 1, len(s)):
                if s[start:j+1] == s[start:j+1][::-1]:
                    state.append(s[start:j+1])
                    bt(state, j + 1)
                    state.pop()
            return


        bt([], 0)
        return palindromes