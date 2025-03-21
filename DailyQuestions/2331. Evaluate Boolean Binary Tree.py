class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)

        if root.val == 2:
            return l or r
        else:
            return l and r
