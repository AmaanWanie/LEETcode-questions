class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        common = set(nums1).intersection(set(nums2))
        ans=[]
        
        ans.append(list(set(nums1) - common))
        ans.append(list(set(nums2) - common))
        return (ans)
