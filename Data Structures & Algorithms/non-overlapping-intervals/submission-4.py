class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        print(intervals)
        prev_end = float("-inf")
        count = 0

        for s, e in intervals:
            if s < prev_end:
                count += 1
            else:
                prev_end = e
        
        return count