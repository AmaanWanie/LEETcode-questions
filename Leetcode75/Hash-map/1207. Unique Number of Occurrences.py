class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = {}
        for i in arr:
            if i in unique:
                unique[i]+=1
            else:
                unique[i]=0
        if len(set(unique.values())) == len(unique.values()):
            return True
        else:
            return False
