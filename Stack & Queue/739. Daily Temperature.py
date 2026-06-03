class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ Stack: O(n)
        Track (index, temperature) pair, waiting for a warmer day.
        When a warmer day comes, pop stack, record the day gap into res, 
        then push warmer day onto stack
        """
        res = [0] * len(temperatures)
        stack = []     # pair [i, t]

        # Give pair (i, t)
        for i, t in enumerate(temperatures):
            # While stack is not empty and current temp > top of stack
            while stack and t > stack[-1][1]:
                # Pop the top pair
                index, temp = stack.pop()
                res[index] = i - index   # number of days to warmer
            # Record current (warmer) day
            stack.append([i, t])
        
        return res