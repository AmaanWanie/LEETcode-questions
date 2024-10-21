class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = []
        ans = []
        sort = []

        for word in strs:
            t = ''.join(sorted(word))
            sort.append(t)


        i = len(strs) - 1
        
        while len(strs) > 0:

            if i == -1: 
                ans.append(list1)
                list1 = [] 
                i = len(strs) - 1
        
            elif sort[i] == sort[0]:
                list1.append(strs[i])
                strs.pop(i)
                sort.pop(i)  
                i -= 1

            else:
                i -= 1

        if list1:
            ans.append(list1)

        return ans