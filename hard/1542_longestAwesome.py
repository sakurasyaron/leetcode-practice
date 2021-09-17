"""
Given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it palindrome.
Return the length of the maximum length awesome substring of s.
Example 1:
Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
Example 2:
Input: s = "12345678"
Output: 1
Example 3:
Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
Example 4:
Input: s = "00"
Output: 2
"""


class Solution:
    def longestAwesome(self, s: str) -> int:
        prefix_dict = {}
        mask = 0
        prefix_dict[mask] = -1
        awesome_len = 0
        for idx, num in enumerate(s):
            mask ^= 1 << int(num)
            if mask in prefix_dict:
                awesome_len = max(awesome_len, idx - prefix_dict[mask])
            else:
                prefix_dict[mask] = idx
            for j in range(10):
                new_mask = mask ^ (1 << j)
                if new_mask in prefix_dict:
                    awesome_len = max(awesome_len, idx-prefix_dict[new_mask])
        return awesome_len


if __name__ == '__main__':
    s = Solution()
    print(s.longestAwesome("3242415"))  # 5
    print(s.longestAwesome("12345678"))  # 1
    print(s.longestAwesome("213123"))  # 6
    print(s.longestAwesome("00"))  # 2
    print(s.longestAwesome("9498331"))  # 3
    print(s.longestAwesome("76263"))  # 3
