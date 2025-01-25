class Solution:
    def distinctIntegers(self, n: int) -> int:
        result = set()
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if j % i == 1:
                    result.add(i)
        result.add(n)  
        return len(result)
