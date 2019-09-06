# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        a = nums[0]
        for i in nums:
            r = max(r + i, i)
            a = max(a,r)
        return a


        # for i in range(1, len(nums)):
        #     nums[i] = nums[i] + max(nums[i - 1], 0)
        # return max(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
