# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head3 = ListNode(0)
        list3 = head3
        while list1 and list2:
            if list1.val <= list2.val:
                head3.next = list1
                head3 = head3.next
                list1 = list1.next
            else:
                head3.next = list2
                head3 = head3.next
                list2 = list2.next
        if list1 :
            head3.next = list1
        else:
            head3.next = list2
        return list3.next