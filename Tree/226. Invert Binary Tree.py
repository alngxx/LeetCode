# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Iterative DFS using Stack """
        if not root:
            return None
        stack = [root]

        # Pop top node & swap its children until stack is empty
        while stack:
            node = stack.pop()  # Take the top node
            # Swap its children
            node.left, node.right = node.right, node.left

            # Push its children to stack (if exists)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
