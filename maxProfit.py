# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        a = 0x3f3f3f3f
        for i in range(0,len(prices)):
            a = min(a,prices[i])
            r = max(r, prices[i] - a)
        return r

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))