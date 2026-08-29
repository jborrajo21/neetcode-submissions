"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((0, interval.start))
            times.append((1, interval.end - 1))
        
        times.sort(key=lambda x: x[0])
        times.sort(key=lambda x: x[1])

        rooms = 0
        active = 0
        for time in times:
            if time[0] == 0:
                active += 1
                rooms = max(rooms, active)
            else:
                active -= 1
        
        return rooms

