class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            total_sum = 0
            while number:
                digit = number % 10
                total_sum += digit * digit
                number //= 10
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
        
