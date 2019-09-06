# -*- coding: utf-8 -*-
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0,1,2]
        for i in range(2,n):
            f.append(f[i-1] + f[i])
        return f[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))