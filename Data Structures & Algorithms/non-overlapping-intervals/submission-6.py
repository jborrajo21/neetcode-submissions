class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if prev_end > start:
                count += 1
            else:
                prev_end = end
            
        return count