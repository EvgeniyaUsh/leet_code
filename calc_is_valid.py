"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

s = "([])"


def is_valid(s):
    stack = []
    characters = {"(": ")", "{": "}", "[": "]"}
    for ss in s:
        if ss in characters:
            stack.append(ss)
        elif len(stack) == 0 or ss != characters[stack.pop()]:
            return False
    return True


result = is_valid(s)
print(result)
