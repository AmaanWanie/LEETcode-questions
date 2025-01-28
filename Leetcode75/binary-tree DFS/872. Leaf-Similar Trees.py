# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1=[]
        r2=[]
        def recur1(root):
            if root == None:
                return 
            recur1(root.left)
            recur1(root.right)
            if (root.left == None) and (root.right == None):
                r1.append(root.val)

        def recur2(root):
            if root == None:
                return 
            recur2(root.left)
            recur2(root.right)
            if (root.left == None) and (root.right == None):
                r2.append(root.val)

        recur1(root1)
        recur2(root2)

        return r1==r2
