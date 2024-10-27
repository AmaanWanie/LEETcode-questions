class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_vol = 0

        while(i<j):
            
            if height[i] < height[j]:
                h = height[i]
            else:
                h = height[j]

            vol = (j-i) * h
            
            if vol > max_vol:
                max_vol = vol
            #volume

            if height[i] < height[j] :
                i+=1
            else:
                j-=1
            
        return max_vol
