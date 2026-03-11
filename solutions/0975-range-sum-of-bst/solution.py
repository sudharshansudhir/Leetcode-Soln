# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s=[]
        def inorder(root):
            if root:
                inorder(root.left)
                if root.val<=high and root.val>=low:
                    s.append(root.val)
                inorder(root.right)
        inorder(root)
        return sum(s)
