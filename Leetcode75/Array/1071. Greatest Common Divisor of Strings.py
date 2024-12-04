class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a,b):
            if a == 0:
                return b
            elif b == 0:
                return a
            return gcd(b,a%b)
        
        if str1+str2 == str2 + str1:
            x = gcd(len(str1),len(str2))
            return str1[:x]

        
        return ""
