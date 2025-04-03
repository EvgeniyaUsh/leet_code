"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

s = "anagram"
t = "nagaram"


# nlogn
def is_anagram(s, t):
    sorted_s = "".join(sorted(s))
    sorted_t = "".join(sorted(t))
    print(sorted(s), sorted(t))
    if sorted_s == sorted_t:
        return True
    return False


# n
def is_anagram_hash(s, t):
    hash_s = {}
    hash_t = {}
    for ss in s:
        hash_s[ss] = hash_s.get(ss, 0) + 1
    for tt in t:
        hash_t[tt] = hash_t.get(tt, 0) + 1

    return hash_s == hash_t


result = is_anagram(s, t)
print(result)
