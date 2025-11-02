# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to set for O(1) lookup
        delete = set(nums)
        """ Don't use Dummy node
        while head and head.val in delete:      # Handle head removal
            head = head.next

        cur = head
        while cur and cur.next:
            if cur.next.val in delete:
                cur.next = cur.next.next        # Skip next node if in nums
            else:
                cur = cur.next                  # Else, move forwards 
        return head
        """

        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur:
            if cur.val in delete:
                prev.next = cur.next
            else:
                prev = cur
            # Move cur after every check
            cur = cur.next
        return dummy.next
