import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        #  1      2    3     4
        #  10hr  6hr  5hr    4hr

        l = 1
        r = max(piles)
        

        while(l<=r):
            mid = (l+r)//2
            hour = 0
            for i in piles:
                hour += math.ceil(i/mid)
            if hour <= h:
                r = mid-1
            else :
                l = mid+1
        return(l)
