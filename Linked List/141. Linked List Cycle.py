# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Intuition: Tortoise and Hare problem
            If there exists a cycle, fast will eventually meets slow
            slow moves 1 step
            fast moves 2 steps
        '''
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # Check after every move if fast hit slow
            if fast == slow:
                return True  # Exits if hit - cycle found

        # The loop stops only when fast = None
        # Hence, never True outside loop
        return False
