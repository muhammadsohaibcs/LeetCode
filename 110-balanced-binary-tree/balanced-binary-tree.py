# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            def height(root):
                if not root:
                    return 0
                return max(1+height(root.left) ,1+ height(root.right) )
            lheight = height(root.left)
            rheight = height(root.right)
            result = lheight-rheight in [-1,0,1]
            return  result and self.isBalanced(root.left) and self.isBalanced(root.right)

