"""
Given an integer array bloomDay, an integer m and an integer k.
We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
"""

from typing import List, Tuple, Set


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        diff_days = sorted(set(bloomDay))
        if m * k <= len(bloomDay):
            i = 0
            j = len(diff_days) - 1
            if self.groupFlowers(bloomDay, diff_days[i], k) >= m:
                return diff_days[i]
            while i + 1 < j:
                mid = (i + j) // 2
                if self.groupFlowers(bloomDay, diff_days[mid], k) >= m:
                    j = mid
                else:
                    i = mid
            return diff_days[j]
        return -1

    def groupFlowers(self, bloomDay: List[int], day: int, k: int) -> int:
        groups = 0
        count = 0
        for x in bloomDay:
            if x - day > 0:
                count = 0
            else:
                count += 1
                if count == k:
                    count = 0
                    groups += 1
        return groups


if __name__ == '__main__':
    s = Solution()
    print(s.minDays([1, 10, 3, 10, 2], 3, 1))
    print(s.minDays([1, 10, 3, 10, 2], 3, 2))
    print(s.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
    print(s.minDays([1000000000, 1000000000], 1, 1))
    print(s.minDays([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2))
    print(s.minDays([1, 2, 4, 9, 3, 4, 1], 2, 2))

    """
    3
    -1
    12
    1000000000
    9
    4
    """