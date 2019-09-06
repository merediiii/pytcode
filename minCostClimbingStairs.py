# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        r = [0,0]
        for i in range(2, len(cost)+1):
            r.append(min(r[i - 1] + cost[i-1], r[i - 2] + cost[i - 2]))
        return r[len(cost)]


if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
