'''
11. Container With Most Water

1.Initialize Pointers and Variables: Set i to 0, j to the last index, and max_vol to 0.

2.Calculate Volume: In a loop, calculate the volume using the smaller height between height[i] and height[j], and update

  max_vol if the calculated volume is greater.

3.Adjust Pointers: Increment i if height[i] is smaller; otherwise, decrement j.

4.Return Result: Continue the loop until i is no longer less than j, then return max_vol.


'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_vol = 0
        while(i<j):
            if heights[i] < heights[j]:
                h = heights[i]
            else:
                h = heights[j]

            vol = (j-i) * h
            
            if vol > max_vol:
                max_vol = vol
            #volume

            if heights[i] < heights[j] :
                i+=1
            else:
                j-=1
        return max_vol

