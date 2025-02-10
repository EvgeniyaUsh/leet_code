"""
Given a string s that contains parentheses and letters,
remove the minimum number of invalid parentheses to make the input string valid.
Return a list of unique strings that are valid with the minimum number of removals.
You may return the answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]


Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""

s = "()())()"


def remove_invalid_parentheses(s):
    def is_valid(s):
        i = 0
        ctr = 0
        while i < len(s):
            if s[i] == "(":
                ctr += 1
            elif s[i] == ")":
                if ctr == 0:
                    return False
                ctr -= 1

            i += 1
        return ctr == 0

    level = {s}

    while True:
        valid = list(filter(is_valid, level))
        if valid:
            return valid
        level = {s[:i] + s[i + 1 :] for i in range(len(s)) for s in level}


result = remove_invalid_parentheses(s)
print(result)
