"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
"""

nums = [1, 1]


def find_disappeared_numbers(nums):
    n = len(nums)
    result = []
    for i in range(1, n + 1):
        if i not in nums:
            result.append(i)
    return result


d_nums = find_disappeared_numbers(nums)
print(d_nums)
