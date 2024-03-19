# https://leetcode.com/problems/palindrome-linked-list/description/
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val    # 해당 노드의 값
#         self.next = next  # 포인터 역할

def isPalindrome(head):

    num = len(head)
    for i in range(int(num/2)):
        if (head[i] == head[num-i-1]):
            continue
        else:
            return False

    return True

head = [1,2,2,1]
print(isPalindrome(head))