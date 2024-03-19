# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ret_list = ListNode()
        current = ret_list
        temp_carry = 0

        while l1 or l2 or temp_carry:
            val = temp_carry + l1.val + l2.val
            temp_carry = val // 10
            current.next = ListNode(val % 10)
            current = current.next

            l1 = l1.next
            l2 = l2.next

        return ret_list.next

# l1: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# l2: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Solution 클래스의 인스턴스 생성
solution = Solution()

# 두 연결 리스트를 더하여 결과 연결 리스트 얻기
result = solution.addTwoNumbers(l1, l2)

# 결과 출력
while result is not None:
    print(result.val, end=" ")
    result = result.next