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
        #     nums[i] = nums[i] + max(nums[i - 1], 0)       #   nums[i-1]是前i-1项最大连续子序和，其中max(nums[i-1],0)是因为如果最大连续子序和必不可能加上一个负数
        #                                                   #   所以nums[i] + nums即是前i项最大连续子序和，所以第n项nums[n]即是该数组里的最大连续子序和
        # return max(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
