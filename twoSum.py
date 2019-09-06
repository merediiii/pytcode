# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}    #字典
        for i, num in enumerate(nums):
            another_num = target - num
            if another_num in map:
                return [map[another_num], i]
            map[num] = i
        return None


if __name__ == '__main__':
    so = Solution()
    print(so.twoSum([2, 7, 11, 15], 9))
