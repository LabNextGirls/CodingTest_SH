# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# 연결 리스트를 입력받아 페어 단위로 스왑하라

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

         # 헤드 노드가 비어있거나, 다음 노드가 없으면 그대로 반환
        if not head or not head.next:
            return head

        # 결과를 저장할 더미 노드 생성
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next, second.next = second.next, first
            current.next = second # 이게 왜 들어가야 돌아가지? 
            # cur의 next를 update 해야 그다음 문장이 제대로 돌지! 

            current = current.next.next
            
        return dummy.next
    
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# 결과 확인 
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original linked list:")
print_linked_list(head)

solution = Solution()
result = solution.swapPairs(head)

print("Linked list after swapping pairs:")
print_linked_list(result)



# 다른 풀이 - val 만 교환하기 // 사실 이래도 okay

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head