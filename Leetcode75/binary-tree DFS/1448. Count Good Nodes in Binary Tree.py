#initial thoughts: to use basic DFS and if there is no greater node from root to curr node in-beteewn thats why i'll use a maxval var which will keep the track of max val from root.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #>=
        def rec(node,count,maxval):

            if node is None:
                return count
            
            if node.val >= maxval:
                count+=1
                maxval=node.val

            left,right = node.left , node.right

            if left:
                
                count = rec(left,count,maxval)
            if right:
                
                count = rec(right,count,maxval)
            return count
        
        return rec(root,0,root.val)
            
