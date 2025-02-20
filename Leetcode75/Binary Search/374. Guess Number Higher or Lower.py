class Solution:
    def guessNumber(self, n: int) -> int:
        i=1
        def bs(i,n):
            mid = (i+n)//2
            res = guess(mid)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                return bs(i,mid-1)
            else:
                return bs(mid+1,n)
        return bs(i,n)

