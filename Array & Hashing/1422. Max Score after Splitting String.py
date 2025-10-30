class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count("1")  # Number of 1 -> O(n)
        zero = 0
        max_score = 0  # max_score = one + zero

        # Iterate the sequence except last number
        for i in range(len(s) - 1):
            # Decrement number of 1 as pointer move right if it's 1
            if s[i] == "1":
                one -= 1
            # Increment number of 0 as pointer move right if it's 0
            else:
                zero += 1
            # Update max score after each iteration
            max_score = max(max_score, one + zero)
        return max_score
