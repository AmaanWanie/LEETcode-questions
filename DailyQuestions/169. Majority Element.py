class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        threshold = len(nums) // 2
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1   
            if hm[num] > threshold:
                return num
