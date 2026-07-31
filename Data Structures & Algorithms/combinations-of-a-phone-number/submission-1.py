class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
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