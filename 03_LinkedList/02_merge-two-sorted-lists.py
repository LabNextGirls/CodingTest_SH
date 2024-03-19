# https://leetcode.com/problems/merge-two-sorted-lists/description/

# 정렬되어 있는 두 연결 리스트를 합쳐라.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1, list2):
    merged_list = []

    list1.reverse()
    list2.reverse()

    min1 = 0
    min2 = 0

    while(len(list1) != 0 and len(list2) != 0):
        min1 = list1.pop() 
        min2 = list2.pop() 

        if min1 < min2 :
            merged_list.append(min1)
            merged_list.append(min2)
        else:
            merged_list.append(min2)
            merged_list.append(min1)

    return merged_list

list1 = [1,2,4]
list2 = [1,3,4]
print(mergeTwoLists(list1, list2))