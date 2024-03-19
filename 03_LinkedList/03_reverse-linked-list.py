# https://leetcode.com/problems/reverse-linked-list/description/
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverseList(head):
    head.reverse()
    return head

head = [1,2,3,4,5]
print(reverseList(head))



## Solution1 - 재귀 호출

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

# 입력으로 사용할 리스트를 연결 리스트로 변환하는 함수
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# 입력 리스트
head_list = [1, 2, 3, 4, 5]

# 입력 리스트를 연결 리스트로 변환
head_node = create_linked_list(head_list)

# Solution 클래스의 인스턴스 생성
solution = Solution()

# reverseList 메서드 호출
reversed_head = solution.reverseList(head_node)
print(reversed_head)



# Solution2 - 반복 구조

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev