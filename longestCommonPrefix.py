# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) == 0: return ""
        # a = 0;b = 0;minlen = 0x7f7f7f7f
        # for i in strs:
        #     minlen = min(len(i),minlen)
        # for i in range(minlen):
        #     for j in range(len(strs)):
        #         if strs[0][i] == strs[j][i]:
        #             continue
        #         else:
        #             b = 1
        #             break
        #     if b == 1:
        #         if a == 0:
        #             return ""
        #         else:
        #             break
        #     a+=1
        # return strs[0][:a]
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
