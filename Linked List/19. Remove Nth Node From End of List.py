# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ Brute force """
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        # Index of remove node
        remove = len(nodes) - n
        # If remove node is head, return head.next as new head
        if remove == 0:
            return head.next

        # Link the previous node to next node after removed node
        nodes[remove - 1].next = nodes[remove].next

        return head
