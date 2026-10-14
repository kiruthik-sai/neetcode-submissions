# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res=[]
        dq=deque([root])
        while len(dq)>0:
            level=[]
            for _ in range(len(dq)):
                node=dq.popleft()
                level.append(node.val)
                for child in [node.left,node.right]:
                    if child is not None:
                        dq.append(child)
            res.append(level)
        return res




        