# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return True
            def height(root):
                if not root:
                    return 0
                return max(1+height(root.left) ,1+ height(root.right) )
            lheight = height(root.left)
            rheight = height(root.right)
            return lheight-rheight in [-1,0,1] and check(root.left) and check(root.right)
        return (check(root))

