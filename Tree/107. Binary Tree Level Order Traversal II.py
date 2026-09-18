# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ Same as BFS + Queue - Leetcode 102
        Just return res[::-1]
        """
        if not root:
            return []
        
        res = []
        q = deque([root])

        while q:
            cur_level = []
            for _ in range(len(q)):
                node = q.popleft()
                cur_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(cur_level)
        
        return res[::-1]