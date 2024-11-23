class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        gain.insert(0,0)
        for i in range(0,len(gain)-1):
            
            gain[i+1]+=gain[i]
            if gain[i+1]>mx:
                mx = gain[i+1]
                
        return mx

