# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:

        a=[]
        
        def preorder(node):
            if node is None:
                return 

            a.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        
        return a
        