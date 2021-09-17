"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
Example 3:
Input: x = 120
Output: 21
Example 4:
Input: x = 0
Output: 0
"""


class Solution(object):
    def valid_number(self, x):
        if (-1 * 2 ** 31) < x < (2 ** 31 - 1):
            return True
        else:
            return False

    def reverse(self, x):
        if x < 0:
            mul = -1
            x = abs(x)
        else:
            mul = 1
        x_str = str(x)
        x_str = x_str[::-1]
        x = mul * int(x_str)
        if self.valid_number(x):
            return x
        else:
            return 0
