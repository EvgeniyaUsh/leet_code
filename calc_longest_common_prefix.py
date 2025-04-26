"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

strs = ["flower", "flow", "flight"]


def longest_common_prefix(strs):
    str_1 = strs[0]
    res = ""

    counter = 0
    for i in strs:
        len_i = len(i)

        if len_i == 0:
            return res

        if counter == 0 or counter > len_i:
            counter = len(i)

    for i in range(counter):
        for s in strs[1:]:
            if str_1[i] != s[i]:
                return res
        res += str_1[i]
    return res


def longest_common_prefix_best_decision(strs):
    pref = strs[0]
    for s in strs[1:]:
        l = len(pref) if len(pref) < len(s) else len(s)

        i = 0
        while i < l and pref[i] == s[i]:
            i += 1

        pref = pref[:i]

    return pref


res = longest_common_prefix_best_decision(strs)
print(res)
