class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        i=0
        j=len(s)
        while i < j:
            stk.append(s[i])
            if stk[-1] == '*':
                stk.pop()
                stk.pop()
            i+=1
        return "".join(stk)

                