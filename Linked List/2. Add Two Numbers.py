# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        top = l1  
        ans = l2  

        while top or carry:
            
            val1 = top.val if top else 0
            val2 = l2.val if l2 else 0
            temp = val1 + val2 + carry

            
            if temp >= 10:
                l2.val = temp % 10
                carry = 1
            else:
                l2.val = temp
                carry = 0

            
            top = top.next if top else None
            
            if l2.next is None and (top or carry):
                l2.next = ListNode(0)  # Add a new node
            l2 = l2.next
        
        return ans
