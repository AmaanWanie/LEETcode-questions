class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        ni = [0] * len(nums)
        nr = [0] * len(nums)
        
        for i in range(1, len(nums)):
            ni[i] = ni[i - 1] + nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            nr[i] = nr[i + 1] + nums[i + 1]
        
        for i in range(len(nums)):
            if ni[i] == nr[i]:
                return i
        
        return -1
