class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        ops={"+","-","*","/"}
        for i in tokens:
            if i not in ops:
                stk.append(i)
    
            else:
                
                v=float(stk.pop())
                u=float(stk.pop())
                if i =="+":
                    t=u+v
                elif i == "-":
                    t=u-v
                elif i == "*":
                    t=u*v
                else:
                    t=u/v

                stk.append(str(int(t)))
                
        return int(stk[0])
        
