#initial thoughts: i would use a queue DS to push nodes at each level in each iteration and take the last element and push it into aswer.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        Q = []
        Q.append(root)
        ans=[]
        ans.append(root.val)

        while Q:
            l = len(Q)
            for i in range(l):
                node = Q.pop(0)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            if Q:
                ans.append(Q[-1].val)
        return ans