class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        
        # Calculate
        d = (sumAlice - sumBob) // 2
        
        bobSet = set(bobSizes)
        
        for x in aliceSizes:
            y = x - d
            if y in bobSet:
                return [x, y]
