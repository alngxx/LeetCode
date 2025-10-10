# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ Sol 1: Extra O(n) space """
        # Linked List -> Array
        node = []
        cur = head
        while cur:
            node.append(cur.val)
            cur = cur.next

        # Swap elements array
        node[k - 1], node[-k] = node[-k], node[k - 1]

        # Array -> Linked List
        cur = head
        for i in node:
            cur.val = i
            cur = cur.next

        return head

        """ Sol 2: Two Pointers """
