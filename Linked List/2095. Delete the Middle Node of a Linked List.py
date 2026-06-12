class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Find prev_slow, node before middle node
        prev_slow = None
        slow, fast = head, head
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        # Edge case: when head has only 1 node, prev_slow = None
        if prev_slow is None:
            return None     # only node, delete it

        # 2. Link - skip the middle node (slow)
        prev_slow.next = slow.next

        return head