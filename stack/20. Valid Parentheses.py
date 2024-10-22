class Solution:
    def isValid(self, s: str) -> bool:
        Dmap={"[":"]","{":"}","(":")"}
        stack=[]
        
        for i in s:
            
            if i in Dmap:
                stack.append(i)
                
            else: 
                if not stack or i!=Dmap[stack.pop()]:
                    return False

        if stack:
            return False
        else:
            return True
