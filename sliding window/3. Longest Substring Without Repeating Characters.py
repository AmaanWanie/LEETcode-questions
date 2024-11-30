class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hm = dict()
        mx = 0
        start=0

        for i,c in enumerate(s):
            if c in hm and hm[c]>=start:
                start = hm[c]+1
            
            hm[c] = i
            mx = max(mx,i-start+1)

        return mx
        