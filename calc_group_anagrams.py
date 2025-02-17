"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
"""

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(strs):
    grouped = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s not in grouped:
            grouped[sorted_s] = [s]
        else:
            grouped[sorted_s].append(s)

    return list(grouped.values())


result = group_anagrams(strs)
print(result)
