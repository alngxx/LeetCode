class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition: Two pointers
        - cur traverse the original list
        - prev points to correct inserted positoin of the new list
        E.g. 4 -> 2 -> 1 -> 3
        """
        # dummy points to head of new sorted list
        dummy = ListNode(0)  # 0 -> None
        cur = head  # cur = 4

        while cur:
            # Initial, prev points to dummy (head of new list)
            prev = dummy  # prev = 0
            # Move prev forwards until prev.next >= cur.val, so insert cur into prev position
            while prev.next and prev.next.val < cur.val:
                prev = prev.next

            # Save next node of cur before insert cur into new list
            next_node = cur.next

            # Insert cur into new list at prev's position: prev -> cur -> prev.next
            cur.next = prev.next  # 4 -> None
            prev.next = cur  # 0 -> 4 -> None

            # Traverse the original list
            cur = next_node  # cur = 2

        # Return head of new list (except dummy)
        return dummy.next
