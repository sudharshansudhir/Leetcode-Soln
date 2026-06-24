# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr=[]
        def traverse(root):
            if root:
                traverse(root.left)
                self.arr.append(root.val)
                traverse(root.right)
            return 
        traverse(root)
        self.i=0


    def next(self) -> int:
        # print(self.arr,self.i)
        if self.i<len(self.arr):
            self.i+=1
            return self.arr[self.i-1]
        

    def hasNext(self) -> bool:
        if self.i<len(self.arr):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()