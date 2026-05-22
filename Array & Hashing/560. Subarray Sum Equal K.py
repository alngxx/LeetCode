class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """ Hash Map: O(n) 
        Intuition: If prefix[j] - prefix[i] = k, then subarray (i, j] sums to k 
        So for each position j, count how many previous prefix sums equal diff = total - k
        """
        # prefix_sum =  how many times this sum has appeared so far
        # Edge case: handle when subarray start from index 0
        prefix_sum = {0 : 1}  # empty prefix (sum = 0), count 1
        total = 0    # current sum
        count = 0 

        for num in nums:
            total += num
            diff = total - k

            if diff in prefix_sum:
                count += prefix_sum[diff]     # how many subarray ending here sum = k
            prefix_sum[total] = prefix_sum.get(total, 0) +  1  # record this prefix sum
        
        return count