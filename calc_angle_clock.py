"""
Given two numbers, hour and minutes, return the smaller angle (in degrees)
formed between the hour and the minute hand.
Answers within 10-5 of the actual value will be accepted as correct.

Example 1:

Input: hour = 12, minutes = 30
Output: 165

Example 2:

Input: hour = 3, minutes = 30
Output: 75

Example 3:

Input: hour = 3, minutes = 15
Output: 7.5
"""

hour = 3
minutes = 15


def angle_clock(hour: int, minutes: int) -> float:
    minutes_angle = 6 * minutes

    diff_hour = minutes / 10 * 5

    hour_angle = 30 * hour + diff_hour

    angle = abs(hour_angle - minutes_angle)

    return min(angle, 360 - angle)


nums1 = [2, 2]
nums2 = [1, 2, 3, 2, 8, 1]


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    result_list = []
    for num in nums1:
        if num in nums2:
            result_list.append(num)
            nums2.remove(num)
    return result_list


res = intersect(nums1, nums2)
print(res)
