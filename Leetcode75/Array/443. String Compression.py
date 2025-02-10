
class Solution:
    def compress(self, chars: List[str]) -> int:
        cpr = ""
        j = 0 
        
        for i in range(len(chars)):

            if i + 1 == len(chars) or chars[i] != chars[i + 1]:
                count = i - j + 1
                cpr += chars[j]
                
                if count > 1:
                    cpr += str(count)
                j = i + 1
                
        chars[:] = list(cpr)
        return len(chars)
