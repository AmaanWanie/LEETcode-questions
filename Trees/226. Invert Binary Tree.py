# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = root

        def rec(temp):
            if temp == None:
                return
            
            rec(temp.left)
            rec(temp.right)
            a = temp.left
            temp.left = temp.right
            temp.right = a
        
        rec(temp)#1
        return root
        