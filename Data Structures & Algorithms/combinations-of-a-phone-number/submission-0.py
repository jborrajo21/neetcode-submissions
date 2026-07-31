class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": {"a", "b", "c"},
            "3": {"d", "e", "f"},
            "4": {"g", "h", "i"},
            "5": {"j", "k", "l"},
            "6": {"m", "n", "o"},
            "7": {"p", "q", "r", "s"},
            "8": {"t", "u", "v"},
            "9": {"w", "x", "y", "z"},
        }

        combs = []

        def bt(state, start):
            if start == len(digits):
                combs.append(str(state))
                return
            
            for letter in letters[digits[start]]:
                bt("".join([state, letter]), start + 1)
            return
        
        if not digits: return []
        bt("", 0)
        return combs