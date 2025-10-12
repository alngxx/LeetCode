# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Sol 1: Linked List -> Array
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        # From now, nodes is a list stores references to each node in LL
        remove_index = len(nodes) - n
        # Special case: If removeIndex is head, return head.next as new head
        if remove_index == 0:
            return head.next

        # Link previous node to next node after removed node
        nodes[remove_index - 1].next = nodes[remove_index].next

        return head

        # Sol 2: Modify in-place


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Create dummy always point to head in case we remove head
        first = second = dummy

        # Move first to (n+1)th_node from start
        for _ in range(1, n + 1):
            first = first.next

        # When first reach the end, second is right before the node we want to remove
        while first.next:
            first = first.next  # first.next = None
            second = second.next  # second = (n-1)th_node from the end now

        # Remove nth_node from the end
        second.next = second.next.next

        return dummy.next
