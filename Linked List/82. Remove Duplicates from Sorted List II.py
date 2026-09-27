class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """ Two Pointers: O(n), O(1)
        1. prev = last distinct node
        2. If cur == cur.next , skip all duplicates until cur != cur.next
        3. Then prev.next = cur.next
        4. Advance cur every step
        """
        dummy = ListNode(0, head)       # in case remove head
        cur = dummy.next
        prev = dummy

        while cur and cur.next:
            if cur.val == cur.next.val:
                # advance cur until cur.val != cur.next.val
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # while loop exists when cur.next = new node found
                # connect prev to that node after duplicates
                prev.next = cur.next
            
            else:
                prev = prev.next
            cur = cur.next
        
        return dummy.next