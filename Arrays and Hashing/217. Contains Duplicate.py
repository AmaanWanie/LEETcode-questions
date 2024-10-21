class Solution(object):
    def containsDuplicate(self, nums):
        Dmap={}
        for n in nums:
            if n in Dmap:
                return True
            else:
                Dmap[n]=1
        return False
        