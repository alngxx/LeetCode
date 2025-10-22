class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """ Intuition: If two prefix sums have the same remainder, then the subarray between them has a sum that is divisible by k
        If prefix[j] % k == prefix[i-1] % k
        → (prefix[j] - prefix[i-1]) % k == 0
        → subarray(i, j) is divisible by k
        """
        # dict store frequency of remainder so far
        remainder_count = {0: 1}  # Init, sum = 0 -> remainder 0 appear once
        total = 0
        count = 0

        for num in nums:
            total += num  # current prefix sum
            remainder = total % k  # remainder of current prefix sum

            # If remainder already in dict, then subarray between two prefix sum divisible by k
            if remainder in remainder_count:
                count += remainder_count[remainder]

            # Update count of that remainder
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return count
