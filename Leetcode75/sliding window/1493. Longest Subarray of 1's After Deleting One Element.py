class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = 0
        zero=0
        i,j=0,0
        while (j<len(nums)):
            if nums[j] == 0:
                zero+=1
            j+=1
            
            while zero > 1:
                if nums[i] ==0:
                    zero-=1
                i+=1
            
            maxSum=max(maxSum,j-i-1)
        return maxSum

