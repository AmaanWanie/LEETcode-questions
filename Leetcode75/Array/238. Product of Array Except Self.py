class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_l = [1]*len(nums)
        n_r = [1]*len(nums)
        n_f = [1]*len(nums)
        
        for i in range(1,len(nums)):
            n_l[i]=nums[i-1] * n_l[i-1]

        for i in range(len(nums)-2,-1,-1):
            n_r[i]=nums[i+1] * n_r[i+1]

        for i in range(len(nums)):
            n_f[i]=n_l[i] * n_r[i]
        
        return n_f

       
