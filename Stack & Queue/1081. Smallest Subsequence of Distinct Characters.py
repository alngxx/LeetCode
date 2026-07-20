class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """ Greedy: O(n), O(1)
        1. Count total count of each char (need this to know if a char reappears later)
        2. Scan s left to right, building an answer stack
        3. Skip a char if it's already placed in the stack (each char used exactly once)
        4. Before placing current char, pop off the top of the stack while:
            - top is bigger than current char (order would improve by swapping)
            - top still appears later in s (safe to remove now, we'll get another chance)
        5. Push current char, mark it visited
        6. Join stack at the end
        """
        count = {c : 0 for c in s}
        for c in s:
            count[c] += 1
        
        visited = set()
        stack = []

        for c in s:
            count[c] -= 1
            # if already visited, skip (keep only first occurence)
            if c in visited:
                continue
            # pop worse chars off top: bigger than c AND still appears later
            while stack and stack[-1] > c and count[stack[-1]] > 0:
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        
        return "".join(stack)