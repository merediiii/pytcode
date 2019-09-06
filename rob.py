# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:return 0
        if len(nums) == 1:return nums[0]
        r = [nums[0],max(nums[0],nums[1])]
        for i in range(2,len(nums)):
            r.append(max(r[i-2] + nums[i],r[i-1]))
        return r[len(nums)-1]

if __name__ == '__main__':
    s = Solution()
    print(s.rob([2,7,9,3,1]))