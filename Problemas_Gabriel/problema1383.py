from heapq import heappush, heappop
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        min_heap = []  
        speed_sum = 0
        max_perf = 0

        for eff, spd in engineers:
            if len(min_heap) == k:
                removed_speed = heappop(min_heap)
                speed_sum -= removed_speed

            heappush(min_heap, spd)
            speed_sum += spd

            performance = speed_sum * eff
            max_perf = max(max_perf, performance)
        
        return max_perf % MOD