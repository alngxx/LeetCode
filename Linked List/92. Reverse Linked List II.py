class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """ 
        1. Find prev_left to reconnect the list after reverse
        2. Reverse the sublist
        3. Reconnect both ends
        head = [1,2,3,4,5], left = 2, right = 4
        """
        dummy = ListNode(0, head)       
        prev_left = dummy
        cur = head

        # 1. move prev_left.next = left, cur = left
        for _ in range(1, left):
            prev_left = prev_left.next      # prev_left = 1
            cur = cur.next                  # cur = 2

        # 2. reverse from left to right
        prev = None
        for _ in range(left, right + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # 3. connect both ends
        # now: prev = 4, cur = 5
        prev_left.next.next = cur
        prev_left.next = prev

        return dummy.next