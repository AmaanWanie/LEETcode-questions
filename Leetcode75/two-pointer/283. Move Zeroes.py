class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i]='-'
                nums.append(0)
        i=0
        while(i<len(nums)):
            if nums[i] == '-':
                nums.pop(i)
                i-=1
            else:
                i+=1
                
        return nums