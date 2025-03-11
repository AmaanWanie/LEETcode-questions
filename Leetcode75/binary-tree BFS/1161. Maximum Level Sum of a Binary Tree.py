class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 1
        Q=[]
        level=1
        ans = 1
        maxx=root.val
        Q.append(root)
        
        while Q:
            l = len(Q)
            summ = 0
            for i in range(l):
                node = Q.pop(0)
                summ+=node.val
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                
            if summ > maxx:
                ans = level
                maxx = summ
            level+=1
        return ans

