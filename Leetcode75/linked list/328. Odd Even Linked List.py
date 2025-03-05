#inital thoughts: separate the list into two groups even and odd by iterating over i and if i % 2 is 0 (even) then append to even list else odd list


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        oddHead = head
        evenHead = head.next
        i=1
        odd = oddHead
        even = evenHead
        curr = even.next

        while curr:
            if i%2 != 0:
                #odd
                odd.next = curr
                odd = curr
            else:
                even.next = curr
                even = curr
            curr = curr.next
            i+=1
        even.next = None
        odd.next = evenHead
        return oddHead




        
