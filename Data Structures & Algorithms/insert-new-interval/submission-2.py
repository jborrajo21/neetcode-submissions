class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        l,r = 0, len(intervals) - 1
        while l < r:
            mid = (l + r) // 2
            start, end = intervals[mid]
            if start >= newInterval[0]:
                r = mid
            else:
                l = mid + 1
        
        idx = r + 1 if newInterval[0] > intervals[r][0] else r

        res = []
        for i in range(idx):
            s1,e1 = newInterval
            s2,e2 = intervals[i]
            if s1 <= e2 and e1 >= s2:
                newInterval[1] = max(e2,e1)
                newInterval[0] = min(s1,s2)
            else:
                res.append(intervals[i])
            
        res.append(newInterval)

        for i in range(idx, len(intervals)):
            s1,e1 = newInterval
            s2,e2 = intervals[i]
            if s1 <= e2 and e1 >= s2:
                newInterval[1] = max(e2,e1)
            else:
                res.append(intervals[i])
        return res
        