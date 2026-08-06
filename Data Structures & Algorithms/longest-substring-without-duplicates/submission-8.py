class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen and l < r:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, len(seen))
        
        return longest
            
