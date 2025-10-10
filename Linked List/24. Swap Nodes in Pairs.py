""" Intuition: Two Pointers
head -> 1 -> 2 -> 3 -> 4 -> None
- prev: always point to previous node of current pair (prev.next = cur)
- cur: current node
- npn (next_pair_node): store next pair node to link before swapping
"""


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy.value = 0 and always point to head -> return dummy.next
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur and cur.next:
            npn = cur.next.next
            second = cur.next

            # Swap
            second.next = cur
            cur.next = npn
            prev.next = second

            # Move to next pair
            prev = cur
            cur = npn
