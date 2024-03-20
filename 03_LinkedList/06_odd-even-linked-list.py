# https://leetcode.com/problems/odd-even-linked-list/description/
# 주어진 연결 리스트를 홀수 다음에 짝수가 오도록 정렬하기 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None
        
        # even이랑 even_head는 별개로 움직이는 것 ! 
        odd_head = odd = ListNode(0)
        even_head = even = ListNode(0)

        while head:
            # 각자 head 값을 가져가는 것
            if head.val % 2 == 0: 
                even.next = head
                even = even.next 
            else:
                odd.next = head
                odd = odd.next 
            head = head.next # 반복문 역할

        even.next = None # 왜냐하면 리스트의 끝이 되니까
        odd.next = even_head.next # 홀수 리스트가 끝나면 짝수 시작 (헤드는 빈값이라서 다음으로 넘겨)

        # (헤드는 빈값이라서 다음으로 넘겨)
        return odd_head.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(7)

print("Original linked list:")
print_linked_list(head)

solution = Solution()
result = solution.oddEvenList(head)

print("Linked list after rearranging odd and even nodes:")
print_linked_list(result)