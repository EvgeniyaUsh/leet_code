"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

n = 2


def climb_stairs(n):
    if n <= 1:
        return 1

    n1 = 1
    n2 = 2

    for i in range(3, n + 1):
        n1, n2 = n2, n1 + n2
    return n2


result = climb_stairs(5)
print(result)
