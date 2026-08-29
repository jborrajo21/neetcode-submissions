class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        
        res = []

        l = 0

        while l < len(intervals):
            r = l + 1
            while r < len(intervals) and intervals[l][0] <= intervals[r][1] and intervals[r][0] <= intervals[l][1]:
                print(intervals[l], intervals[r])
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
                r += 1
            
            res.append(intervals[l])
            l = r
        
        return res
