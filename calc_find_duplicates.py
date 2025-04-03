from collections import defaultdict

nums = [4, 3, 2, 7, 8, 2, 3, 1]


def find_duplicates(nums):
    result = []
    dict_nums = {}
    for i in nums:
        if i in dict_nums.keys():
            result.append(i)
        dict_nums[i] = 1
    return result


def find_duplicates_2(nums):
    result = [i for i in nums if nums.count(i) > 1]
    # dict_nums = {}
    # for i in nums:
    #     if i in dict_nums.keys():
    #         result.append(i)
    #     dict_nums[i] = 1
    return list(set(result))


result = find_duplicates(nums)
result_2 = find_duplicates_2(nums)
print(result)
