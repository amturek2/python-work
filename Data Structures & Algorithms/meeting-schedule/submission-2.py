"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #start with smallest start first then grab next smallest 
        #start and if it is in between you cannot 

        # sort by first value 
        intervals = sorted(intervals, key = lambda inter: inter.start)
        for i in range(len(intervals) - 1): 
            curr = intervals[i]
            nxt = intervals[i + 1]
            if (nxt.start < curr.end): 
                return False 
        return True