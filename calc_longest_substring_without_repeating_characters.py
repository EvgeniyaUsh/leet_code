# Output: 3
# Explanation: The answer is "abc", with the length of 3.


s = "pwwkewg"


def length_of_longest_substring(s):
    len_ss = 0
    max_len = 0
    list_ss = []
    for count, i in enumerate(s, start=0):
        if count == 0:
            len_ss += 1
        elif i != list_ss[count - 1] and i not in list_ss[count - len_ss : count + 1]:
            len_ss += 1
        else:
            len_ss = 1
        list_ss.append(i)

        if max_len < len_ss:
            max_len = len_ss

        print(count, count - len_ss)
        print(len_ss)
        print(list_ss)

    return max_len


result = length_of_longest_substring(s)
print(result)
