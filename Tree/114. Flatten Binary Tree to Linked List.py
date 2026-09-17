# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """ Iterative Preorder: O(n), O(1)
        1. At each node, if left subtree exists: find rightmost of left subtree
        2. Attach current right to that rightmost node
        3. Attach left to right, set left to None
        4. Move to next node (root.right)
        """
        if not root:
            return None
        cur = root
        
        while cur:                                  # cur = 1
            if cur.left:
                rightmost = cur.left                # rightmost = 2
                while rightmost.right:
                    rightmost = rightmost.right     # rightmost = 4
                rightmost.right = cur.right         # attach 5-6 to 4
                cur.right = cur.left                # attach 2, 3, 4, 5, 6 to 1
                cur.left = None                     # clear left branch
            cur = cur.right                         # cur = 2