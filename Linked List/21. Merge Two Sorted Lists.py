# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if not list1 and not list2:
            return []
        
        if list1.val <= list2.val:
            h1 = list1.next
            h2 = list2
            send = list1
            temp = list1
        else :
            h1 = list1
            h2 = list2.next
            send = list2
            temp = list2
        
        while h1 and h2:
            
            if h1.val <= h2.val:
                temp.next = h1
                temp = h1
                h1 = h1.next
            else:
                temp.next = h2
                temp = h2
                h2 = h2.next
        if not h1:
            temp.next = h2
        else:
            temp.next = h1
        
                
        return send
