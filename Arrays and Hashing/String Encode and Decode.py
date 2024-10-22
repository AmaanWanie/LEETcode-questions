class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "||"
        st="__".join(strs)
        
        return st

    def decode(self, s: str) -> List[str]:
        if s == "||":
            return []

        ans=s.split("__")
        return ans

