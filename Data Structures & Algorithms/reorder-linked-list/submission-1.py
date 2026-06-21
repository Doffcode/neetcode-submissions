class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #make another list
        dummy = ListNode()
        h2 = head
        l1 = dummy
        while(h2):
            dummy.next = ListNode(h2.val)
            h2 = h2.next
            dummy = dummy.next
        l1 = l1.next
        #reverse the new list
        curr = l1
        prev = None
        lenght = 0
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            lenght +=1
        l1 = prev
        head1 = head
        head2 = l1
        dum = ListNode()
        l2 = dum
        while(lenght>0):
            dum.next = head1
            head1 = head1.next
            dum = dum.next
            lenght -=1
            if lenght > 0:
                dum.next = head2
                head2 = head2.next
                dum = dum.next
                lenght -=1
        dum.next = None
        temp = l2.next
        while(temp):
            print(temp.val)
            temp = temp.next
        

