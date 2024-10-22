class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        dmap={}
        times=[]

        for nu in nums:
            
            if nu not in dmap:
                t=nums.count(nu)
                dmap[nu]=t
                times.append(t)
        times.sort(reverse=True)

        for i in range(k):
            for key , value in dmap.items():
                if (times[i]==value)and key not in ans:
                    ans.append(key)
        return ans
        
