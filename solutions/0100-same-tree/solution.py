# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a1=[]
        a2=[]
        h1=p
        def traverse(node):
            if node:
                a1.append(node.val)
                traverse(node.left)
                traverse(node.right)
            else:
                a1.append(None)
        def traverse2(node):
            if node:
                a2.append(node.val)
                traverse2(node.left)
                traverse2(node.right)
            else:
                a2.append(None)
            
        traverse(p)
        traverse2(q)

        print(a1)
        print(a2)

        return a1==a2
