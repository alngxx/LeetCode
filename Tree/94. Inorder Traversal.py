# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # Store nodes inorder

        def inorder(node):
            # E.g. If node.left is None, return inorder(node) to process next (res.append(node.val))
            if not node:
                return

            # recursively traverse left subtree
            inorder(node.left)
            # if node is None, append to res
            res.append(node.val)
            # return to previous node, and recursively traverse its right
            inorder(node.right)

        inorder(root)
        return res
