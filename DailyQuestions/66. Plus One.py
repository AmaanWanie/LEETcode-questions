class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > 9:
                digits[i] = 0
                if i > 0:
                    digits[i - 1] += 1
                else:
                    digits.insert(0, 1)
            else:
                break        
        return digits
