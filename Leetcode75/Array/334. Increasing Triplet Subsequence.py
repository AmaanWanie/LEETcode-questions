class Solution:
  
    def increasingTriplet(self, nums: List[int]) -> bool:
        small=float('inf')
        mid=float('inf')
        i=0
        while(i<len(nums)):
            if nums[i] < small and nums[i] < mid:
                small = nums[i]
            elif nums[i] > small and nums[i] < mid:
                mid = nums[i]
            elif nums[i] > small and nums[i] > mid:
                return True
            i+=1
        return False
            
        
