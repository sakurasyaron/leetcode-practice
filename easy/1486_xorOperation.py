"""
Given an integer n and an integer start.
Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.
Example 1:
Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
Example 2:
Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
Example 3:
Input: n = 1, start = 7
Output: 7
Example 4:
Input: n = 10, start = 5
Output: 2
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor_res = start
        for i in range(1, n):
            xor_res ^= (start + 2*i)
        return xor_res


if __name__ == '__main__':
    s = Solution()
    print(s.xorOperation(5, 0))
    print(s.xorOperation(4, 3))
    print(s.xorOperation(1, 7))
    print(s.xorOperation(10, 5))
