class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        '''
        Intuition
        Build new LL by always link the smaller node to cur.next
        Once one list is empty, link the rest of the other list
        -> O(m+n): Iterate through all elements of two LL
        '''

        # dummy always point to head of new LL
        dummy = ListNode()

        # cur points to last node of new LL. Initally, cur = dummy
        cur = dummy

        # Compare every element of two lists, link the smaller to new list (cur.next)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        # Link the leftovers of list1 or list2
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        # Return new LL
        return dummy.next
