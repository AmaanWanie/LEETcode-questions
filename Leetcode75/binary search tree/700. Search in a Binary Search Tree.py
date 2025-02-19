# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def rec(Node, val):
            if Node is None:
                return None
            elif Node.val == val:
                return Node

            elif Node.val > val:
                return rec(Node.left, val)
            else:
                return rec(Node.right, val)
                
        return rec(root, val)