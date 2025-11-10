import bisect

class SummaryRanges(object):

    def __init__(self):
        self.intervals = []

    def addNum(self, value):
        starts = [i[0] for i in self.intervals]
        index = bisect.bisect_right(starts, value)
        
        prev_interval = None
        if index > 0:
            prev_interval = self.intervals[index - 1]

        next_interval = None
        if index < len(self.intervals):
            next_interval = self.intervals[index]

        if prev_interval and prev_interval[0] <= value <= prev_interval[1]:
            return

        connects_prev = prev_interval and prev_interval[1] == value - 1
        connects_next = next_interval and next_interval[0] == value + 1

        if connects_prev and connects_next:
            self.intervals.pop(index)
            prev_interval[1] = next_interval[1]
            
        elif connects_prev:
            prev_interval[1] = value
            
        elif connects_next:
            next_interval[0] = value
            
        else:
            self.intervals.insert(index, [value, value])

    def getIntervals(self):
        return self.intervals