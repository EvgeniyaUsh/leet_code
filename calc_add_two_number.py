"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    head = ListNode()
    current = head
    carry = 0
    while l1 or l2 or carry != 0:
        l1_value = l1.val if l1 else 0
        l2_value = l2.val if l2 else 0
        total = l1_value + l2_value + carry
        current.next = ListNode(total % 10)
        current = current.next
        carry = total // 10

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return head.next


def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


l1 = create_linked_list([1, 7, 1])
l2 = create_linked_list([0, 9, 1, 1])

result = add_two_numbers(l1, l2)

output = []
while result:
    output.append(result.val)
    result = result.next
print(output)
