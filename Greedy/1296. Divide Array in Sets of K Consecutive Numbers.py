class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """ Hashmap + Sorting: O(n logn), O(n)
        1. Sort + count each number
        2. Iterate every num
        3. If count[num] > 0, start checking new group of size k (since it's not assigned)
        4. For i in (num, num + k), if count[i] = 0, can't form group -> return False
        5. count[i] -= 1 for every group assign
        """
        n = len(nums)
        if n % k != 0:
            return False
        
        nums.sort()
        # Counter(list) auto return 0 for missing key
        count = Counter(nums)
        
        for num in nums:
            # only form new group if num is unused
            if count[num]:
                for i in range(num, num + k):
                    # missing number needed for group
                    if not count[i]:
                        return False
                    count[i] -= 1
        
        return True