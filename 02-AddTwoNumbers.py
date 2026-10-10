# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # @staticmethod
    # def printList(node):
    #     while node is not None:
    #         print(node.val, end="")
    #         if node.next is not None:
    #             print(" -> ", end="")
    #         node = node.next
    #     print()

    # @staticmethod
    # def createList(nums):
    #     dummy = ListNode()
    #     tail = dummy

    #     for num in nums:
    #         tail.next = ListNode(num)
    #         tail = tail.next

    #     return dummy.next

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            # lấy chữ số từ l1 (0 nếu l1 đã hết)
            # lấy chữ số từ l2 (0 nếu l2 đã hết)
            # tính tổng, tách chữ số và carry
            # tạo node mới, nối vào tail, dịch tail
            # dịch l1, l2 sang node kế tiếp (nếu còn)

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x+y+carry
            carry = total // 10

            tail.next = ListNode(total % 10)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


# if __name__ == "__main__":
#     solution = Solution()

#     # Số 342: lưu theo thứ tự ngược 2 -> 4 -> 3
#     l1 = solution.createList([9,9,9,9,9,9,9])

#     # Số 465: lưu theo thứ tự ngược 5 -> 6 -> 4
#     l2 = solution.createList([9,9,9,9])

#     print("List 1:")
#     solution.printList(l1)

#     print("List 2:")
#     solution.printList(l2)

#     result = solution.addTwoNumbers(l1, l2)

#     print("Result:")
#     solution.printList(result)
