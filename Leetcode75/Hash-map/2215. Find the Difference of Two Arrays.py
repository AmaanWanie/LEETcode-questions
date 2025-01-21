class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
	n1 = set(nums1)
	n2 = set(nums2)
        common = n1.intersection(n2)
        ans=[]
        
        ans.append(list(n1 - common))
        ans.append(list(n2 - common))
        return (ans)
