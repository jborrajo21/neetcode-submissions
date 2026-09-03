class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = {}

        for i,c in enumerate(s):
            letters[c] = i
        
        res = []
        i = 0
        while i < len(s):
            j = i
            m = letters[s[i]] + 1
            while j < m:
                m = max(m, letters[s[j]] + 1)
                j += 1
            res.append(j-i)
            i = j

        return res