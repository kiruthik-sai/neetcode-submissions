# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal=True
        def dfs(node):
            if not node:
                return 0

            lefty=dfs(node.left)
            righty=dfs(node.right)
            if abs(lefty-righty) > 1:
                self.bal=False
            return 1 + max(lefty,righty) 
        
        dfs(root)
        return self.bal

            
        