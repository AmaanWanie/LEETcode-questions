# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        j = 0
        t = head

        while t is not None:
            t = t.next
            j += 1

        i = j - n 
        def change(i, head):
            prev = None
            curr = head
            idx = 0  
            while curr is not None:
                if idx == i:
                    if prev is not None:
                        prev.next = curr.next
                    else:
                        head = curr.next
                    break
                prev = curr
                curr = curr.next
                idx += 1
            return head

        return change(i, head)
