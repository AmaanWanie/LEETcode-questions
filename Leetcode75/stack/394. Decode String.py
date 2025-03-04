#inital thought: keep pushing and when encountered a "]" go from beind till '[' and mul th no. before it

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if s[i] != ']':
                stk.append(s[i])
            else:
                subStr = ""
                while stk[-1] != '[':
                    el = stk.pop()
                    subStr= el+subStr
                stk.pop()
                dig = ""
                while stk and stk[-1].isdigit():
                    dig= stk.pop() + dig
                stk.append(int(dig) * subStr)

        return "".join(stk)
            

        

                



