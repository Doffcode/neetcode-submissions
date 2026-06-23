
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #divide the list into the three parts one the left side and other the right side 
        #the middle will be reversed and then join #
        #the end of the left list will be joied to the start of the revlist and the end of the right list will be
        # joined to the start of the right list so for the right list we need just need the head pointer

        # first well get the pos of the left and rightr where we need to break
        if left == right:
            return head
        chead = head
        c1 = c2 = bc1= 1
        blef =  None 
        while chead:
            if c1 == left:
                leftp = chead
            if c2 == right:
                rightp = chead
            if bc1 == left-1:
                blef = chead
            chead = chead.next
            c1+=1
            c2+=1
            bc1+=1
        #till here i tried to get only the pointers


        rlist = rightp.next # this will be the start of the right list
        rightp.next = None # we put the next of the rev list as null
        curr = leftp # i set the curr as the left pointer which is the beg of the left list 
        prev = None
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # now it is reversed
        # i want the tail the rev list didnt i have that as rightp
        leftp.next = rlist
        if blef:
            blef.next = rightp # icould have written it as prev as well ig
            return head
        else:
            return rightp
