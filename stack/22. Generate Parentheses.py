class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []

        def backtrack(open_brace,close_brace):
            if open_brace == close_brace == n:
                res.append("".join(stk))
            if open_brace < n:
                stk.append("(")
                backtrack(open_brace+1,close_brace)
                stk.pop()
            if (close_brace < open_brace):
                stk.append(")")
                backtrack(open_brace,close_brace+1)
                stk.pop()
            
        backtrack(0,0)
        return res
