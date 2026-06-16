from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        q=deque([root])
        z=False
        while q:
            n=len(q)
            lev=[]
            for i in range(n):
                node=q.popleft()
                if node:
                    lev.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if lev:
                if z:
                    ans.append(lev[::-1])
                else:
                    ans.append(lev[:])
                z=not z
        return ans
