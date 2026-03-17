# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root=None
        def insert(root,val):
            if root is None:
                return TreeNode(val)
            if val<root.val:
                root.left=insert(root.left,val)
            else:
                root.right=insert(root.right,val)
            return root
        for i in preorder:
            root=insert(root,i)
        print(root)
        return root

