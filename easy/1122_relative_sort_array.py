from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_counter = Counter(arr1)
        res = [0]*len(arr1)
        cur_index = 0
        for k in arr2:
            if k in arr1_counter:
                count = arr1_counter.pop(k)
                for i in range(cur_index, cur_index+count):
                    res[i] = k
                cur_index += count
        rem_keys = sorted(arr1_counter.keys())
        for k in rem_keys:
            count = arr1_counter.pop(k)
            for i in range(cur_index, cur_index+count):
                res[i] = k
            cur_index += count
        return res


print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))