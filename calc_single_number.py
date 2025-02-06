"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1


Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

nums = [2, 2, 1]


def single_number(nums):
    dict_nums = {}
    for i in nums:
        if i not in dict_nums.keys():
            dict_nums[i] = 1
        else:
            dict_nums[i] += 1

    for k, v in dict_nums.items():
        if v == 1:
            return k


def single_number_xor(nums):
    num = 0
    for n in nums:
        num ^= n
    return num


result = single_number_xor(nums)
print(result)
