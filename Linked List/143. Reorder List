# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        i = head
        j = i.next
        while j and j.next:
            i = i.next
            j = j.next.next
        
        
        j = i.next  
        i.next = None  
        k = j.next if j else None

        while j:
            j.next = i
            i = j
            j = k
            if j:
                k = j.next

        hn = head.next
        iN = i.next
        while True:
            head.next = i
            i.next = hn
            head = hn
            i = iN
            
            if not head or not i:
                break
            
            hn = hn.next if hn else None
            iN = i.next if i else None
