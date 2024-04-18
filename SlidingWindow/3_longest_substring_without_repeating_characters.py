from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        length = 0
        last_index_dict: Dict[str, int] = {}
        for i, c in enumerate(s):
            # if n - i <= max_len - length:
            #     break
            last_index = last_index_dict.get(c)
            if last_index is not None and last_index + length > i:
                length = i - last_index
            else: 
                length += 1
            last_index_dict[c] = i
            max_len = max(max_len, length)
        return max_len
# max_len = 3
# length = 2
# {p: 0, w: 2}
input = "pwwkew"
"""
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
max_len = 3
length = 2
{p: 0, w: 2, k: 3, e: 4}
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""