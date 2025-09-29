class Solution:
    def isValid(self, s: str) -> bool:
        """
        Intuition: O(n)
        - Initialize stack and dict which (key = close : value = open)
        - If we see open bracket (value), push to stack in order
        - Elif we see close bracket (key):
            if stack is empty (no corresponding open bracket before)
            or map[i] != stack.pop() (no correspoding open bracket at the top)
            -> return False
        - Finally, return True if stack is empty (all valid open-close pairs)
        """

        stack = []
        map = {")": "(", "}": "{", "]": "["}

        for i in s:
            # If found open bracket, push to stack
            if i in map.values():
                stack.append(i)

            # Elif found closed bracket, check if there is open bracket before it
            elif i in map.keys():
                if not stack or map[i] != stack.pop():
                    return False

        # If stack empty, return True
        return not stack
