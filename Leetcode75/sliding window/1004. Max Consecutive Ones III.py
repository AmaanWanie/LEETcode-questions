class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxOne=0
        zero = 0
        i,j=0,0
        while j<len(nums):
            if nums[j]==0:
                zero+=1
            j+=1
            if zero <= k:
                maxOne = max(maxOne,j-i)
            elif zero > k:
                while i < len(nums):
                    i+=1
                    if nums[i-1] == 0:
                        zero-=1
                        break
        return maxOne


            


        
