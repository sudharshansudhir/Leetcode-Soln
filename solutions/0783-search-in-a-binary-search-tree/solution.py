# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root,key):
            if root:
                if root.val==key:
                    # print(root,root.val)
                    return root
                if root.val>key:
                    return search(root.left,key)
                else:
                    return search(root.right,key)
            
        return search(root,val)
