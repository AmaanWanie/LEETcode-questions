# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dmap ={}

        while(head is not None):
            if head.next in dmap:
                return True
            else:
                dmap[head.next] = head.val
                head = head.next
        return False
        
