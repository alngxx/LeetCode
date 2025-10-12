# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Intuition: Similar to 100. Same Tree
        """

        def isMirror(n1, n2):
            # Base case: If both left node and right node empty -> return True
            if not n1 and not n2:
                return True
            # Recursive case: Check if mirror
            if n1 and n2 and n1.val == n2.val:
                return isMirror(n1.left, n2.right) and isMirror(n2.left, n1.right)

            return False

        return isMirror(root.left, root.right)
