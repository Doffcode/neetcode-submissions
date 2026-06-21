class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            fast = fast.next
        h1 = slow.next
        slow.next = None

        #reverse the linked list 
        curr = h1
        prev = None
        while(curr):
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp

        h1 = prev
        # now i have to merge the head which will have the half
        # part and the new reversed half which starts from h1
        # starting state is that the head of new list is form head 
        # then after one loop it should be as if the h1 points to 2nd element in 
        # second ll and the head is joined to the list already
        while h1 and head:
            t1 = head.next   #stored the next form first list
            head.next = h1   #added the element form tne 2nd list
            h1 = h1.next     #store the next form the second list  
            head = head.next #moved the head pointer to next value 
            head.next = t1
            head = head.next
        

        