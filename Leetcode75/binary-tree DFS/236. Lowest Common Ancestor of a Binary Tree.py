# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}  
        stack = [root]
        # populate parent
        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # match both the ancestors of p and q , if match return
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent.get(p, None)
        
        while q:
            if q in ancestors:
                return q  
            q = parent.get(q, None)





        
