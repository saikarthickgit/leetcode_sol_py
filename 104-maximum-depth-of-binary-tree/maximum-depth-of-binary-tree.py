# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
            
        left_nod = self.maxDepth(root.left)
        right_nod = self.maxDepth(root.right)
        if root.left is None:
            return 1 + right_nod

        if root.right is None:
            return 1 + left_nod
        
        # Use the results of the recursive calls
        return 1 + max(left_nod, right_nod)
        