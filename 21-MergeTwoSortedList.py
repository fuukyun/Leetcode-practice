# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next

            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next

        # Nối phần còn lại
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
