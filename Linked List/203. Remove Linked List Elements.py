class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Sol 1: Don't use dummy node
        while head and head.val == val:
            head = head.next
        if not head:
            return

        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

        # Sol 2: dummy always to head, hence return dummy.next instead of head
        # If return head, it can be removed in case head.val == val
        dummy = ListNode(0, head)
        cur = dummy

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
