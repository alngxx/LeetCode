# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res = []
        q = deque([root])
        
        while q:
            cur_level = []
            
            # iterate through all nodes at current level
            for _ in range(len(q)):
                node = q.popleft()
                cur_level.append(node.val)

                # add nodes at lower level into queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(cur_level)
        
        return res