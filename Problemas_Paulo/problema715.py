import bisect

class RangeModule(object):

    def __init__(self):
        self.intervals = []

    def addRange(self, left, right):
        starts = [i[0] for i in self.intervals]
        start_index = bisect.bisect_left(starts, left)
        
        if start_index > 0 and self.intervals[start_index - 1][1] >= left:
            start_index -= 1

        end_index = bisect.bisect_right(starts, right)
        
        new_left, new_right = left, right
        
        if start_index < len(self.intervals):
            new_left = min(left, self.intervals[start_index][0])
            
            if end_index > 0:
                new_right = max(right, self.intervals[end_index - 1][1])
            else:
                 new_right = right
        
        new_interval = [new_left, new_right]
        self.intervals[start_index:end_index] = [new_interval]


    def queryRange(self, left, right):
        starts = [i[0] for i in self.intervals]
        index = bisect.bisect_right(starts, left)

        if index > 0:
            covering_interval = self.intervals[index - 1]
            if covering_interval[1] >= right:
                return True
        
        return False

    def removeRange(self, left, right):
        starts = [i[0] for i in self.intervals]
        start_index = bisect.bisect_left(starts, left)
        
        if start_index > 0 and self.intervals[start_index - 1][1] > left:
            start_index -= 1

        end_index = bisect.bisect_right(starts, right)
        
        intervals_to_keep = []
        
        if start_index < len(self.intervals) and self.intervals[start_index][0] < left:
            intervals_to_keep.append([self.intervals[start_index][0], left])
        
        if end_index > 0 and self.intervals[end_index - 1][1] > right:
            intervals_to_keep.append([right, self.intervals[end_index - 1][1]])

        self.intervals[start_index:end_index] = intervals_to_keep