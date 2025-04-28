"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

nums1 = [2, 2]
nums2 = [1, 2, 3, 2, 8, 1]


def intersect_first_solution(nums1: list[int], nums2: list[int]) -> list[int]:
    dict_nums1 = {}
    for n1 in nums1:
        if n1 in dict_nums1.keys():
            dict_nums1[n1] += 1
        else:
            dict_nums1[n1] = 1

    res = []

    for n2 in nums2:
        if dict_nums1.get(n2, 0) > 0:
            res.append(n2)
            dict_nums1[n2] -= 1

    return res


def intersect_second_solution(nums1: list[int], nums2: list[int]) -> list[int]:
    result_list = []
    for num in nums1:
        if num in nums2:
            result_list.append(num)
            nums2.remove(num)
    return result_list


def intersect_sorted(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1.sort()
    nums2.sort()

    i = j = 0
    res = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return res


res = intersect_sorted(nums1, nums2)
print(res)
