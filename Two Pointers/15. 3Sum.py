class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to handle duplicates
        res = []

        # At every fixed element nums[i], assign two pointers j, k
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue

            # Two pointers
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # Move left pointer to find next triplet
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1  # Skip duplicate triplets
        return res
