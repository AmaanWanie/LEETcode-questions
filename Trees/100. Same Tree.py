# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []
        def recur1(root):
            if root is None:
                r1.append(None)
                return 
            r1.append(root.val)
            recur1(root.left)
            recur1(root.right)

        def recur2(root):
            if root is None:
                r2.append(None)
                return 
            r2.append(root.val)
            recur2(root.left)
            recur2(root.right)
        recur1(p)
        recur2(q)
        return r1 == r2
            
        
