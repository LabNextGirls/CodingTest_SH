# https://leetcode.com/problems/reverse-linked-list-ii/description/
# index m부터 n까지 역순으로 만들어라 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution(object):
#     def reverseBetween(self, head, left, right):
#         """
#         :type head: ListNode
#         :type left: int
#         :type right: int
#         :rtype: ListNode
#         """

#         dummy = ListNode()
#         dummy.next = head
#         start_node = dummy
#         end_node = dummy

#         for i in range (left):
#             start_node = start_node.next

#         for i in range (right):
#             end_node = end_node.next

#         while start_node != end_node:
#             temp = start_node
#             temp.next = start_node.next

#             start_node = end_node
#             start_node. next = end_node.next 

#             end_node = temp
#             end_node.next = temp.next 

#             start_node = start_node.next
#             end_node.next = end_node

#         return dummy.next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 예외 처리
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(m - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
print_linked_list(head)

solution = Solution()
result = solution.reverseBetween(head, 2, 4)

print("Linked list after rearranging odd and even nodes:")
print_linked_list(result)