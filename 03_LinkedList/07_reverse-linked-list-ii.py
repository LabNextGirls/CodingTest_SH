# https://leetcode.com/problems/reverse-linked-list-ii/description/
# index m부터 n까지 역순으로 만들어라 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        start_node = ListNode()
        start_node = head 
        end_node = ListNode()
        end_node = head

        for i in range (left):
            start_node = start_node.next
            left = left - 1

        for i in range (right):
            end_node = end_node.next
            right = right - 1

        while (start_node != end_node):
            temp = start_node
            temp.next = start_node.next

            start_node = end_node
            start_node. next = end_node.next 

            end_node = temp
            end_node.next = temp.next 

            start_node = start_node.next
            end_node = end_node.next
        
        return head

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