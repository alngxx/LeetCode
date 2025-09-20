class Solution:
    def countBits(self, n: int) -> List[int]:
        # Function to count 1's in binary form
        def count1(n):
            res = 0
            for i in range(32):
                if (n >> i) & 1:
                    res += 1
            return res

        # Return the list counting number of 1's of each integer up to n
        ans = []
        for i in range(n + 1):
            ans.append(count1(i))
        return ans
