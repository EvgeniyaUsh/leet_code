"""
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

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

s = "pwwkewg"


def length_of_longest_substring(s):
    len_ss = 0
    max_len = 0
    list_ss = []
    for count, i in enumerate(s, start=0):
        if count == 0:
            len_ss += 1
        elif i != list_ss[count - 1] and i not in list_ss[count - len_ss : count + 1]:
            len_ss += 1
        else:
            len_ss = 1
        list_ss.append(i)

        if max_len < len_ss:
            max_len = len_ss

        print(count, count - len_ss)
        print(len_ss)
        print(list_ss)

    return max_len


result = length_of_longest_substring(s)
print(result)
