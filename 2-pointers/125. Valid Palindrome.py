class Solution:
    def isPalindrome(self, s: str) -> bool:
        setis={" ","/","!","'",'"',"?","!",",",".",":","@","#","_","{","}","[","]","/","-",";","(",")","`"}

        s=s.lower()
        check=""
        for i in s:
            if i in setis:
                continue
            else:
                check+=i
    
        i=0
        j=len(check)-1

        while(i<j):
            if check[i]==check[j]:
                i+=1
                j-=1

            else:
                return False
        return True
        
