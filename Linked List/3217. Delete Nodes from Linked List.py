# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to set for O(1) lookup
        delete = set(nums)

        # Handle head removal
        while head and head.val in delete:
            head = head.next

        cur = head
        while cur and cur.next:
            # Skip next node if in nums
            if cur.next.val in delete:
                cur.next = cur.next.next
            # Else, move forwards
            else:
                cur = cur.next

        return head
