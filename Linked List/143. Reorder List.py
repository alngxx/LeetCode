class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find middle (slow)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second halve: L(n) -> L(n-1) -> ... -> L(slow.next)
        cur = slow.next  # Head of the second half
        prev = slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # Link first half with second half - node by node
        first = head  # L0
        second = prev  # L(n)
        while second:
            # Save next node before link
            temp1 = first.next  # temp1 = L1
            temp2 = second.next  # temp2 = L(n-1)

            # Link L0 -> L(n) -> L1 -> ...
            first.next = second
            second.next = temp1

            # Move forwards
            first = temp1
            second = temp2
