"""
Given an array of strings words, return the smallest string that contains each string in words as a substring.
If there are multiple valid strings of the smallest length, return any of them.
You may assume that no string in words is a substring of another string in words.
Example 1:
Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:
Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
Constraints:
1 <= words.length <= 12
1 <= words[i].length <= 20
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List


class Solution:
    def longestSubstring(self, str1: str, str2: str):
        substr_match = ""
        l1, l2 = len(str1), len(str2)
        for i in range(l1):
            match = ""
            for j in range(l2):
                if i+j < l1 and str1[i+j] == str2[j]:
                    match += str2[j]
                elif len(match) > len(substr_match):
                    substr_match = match
                    match = ""
        return substr_match

    def shortestSuperstring(self, words: List[str]) -> str:
        sorted_words = sorted(words, key=len, reverse=True)
        superstring = sorted_words[0]
        for word in sorted_words:
            print(f'{superstring}, {word} : {self.longestSubstring(superstring, word)}')
        return sorted_words


if __name__ == '__main__':
    s = Solution()
    print(s.shortestSuperstring(["alex", "loves", "leetcode"]))
    print(s.shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))
