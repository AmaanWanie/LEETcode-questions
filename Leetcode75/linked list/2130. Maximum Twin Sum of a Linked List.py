# initial thoughts:
# 1) first use slow and fast pointer to find center while pushing the vals of slow to stack till mid point. 
# 2) when this loop finishes , start moving slow ptr again and keep poping the stack and summing them at each interval this way i can mimic the twin sum .
# 3) one going fwd other backwrd due to poping

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
      
        if head.next == None :
            return head.val
        if head.next and head.next.next == None:
            return head.val + head.next.val

        maxx =0
        stk = []
        slow,fast = head,head

        while fast and fast.next:
            stk.append(slow.val)
            slow = slow.next
            fast = fast.next.next
          
        # print(stk)
        while slow:
            v = stk.pop()
            if maxx <= v + slow.val:
                maxx = v + slow.val
            slow = slow.next
        return maxx

