class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time complexity: O(logn)
        # Space complexity: O(1)

        left = 0
        right = len(nums) - 1

        # Loop stops when left > right but still can't find nums[mid] == target
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # If middle element < target, search right half
            elif nums[mid] < target:
                left = mid + 1

            # If middle element > target, search left half
            else:
                right = mid - 1

        # Default value
        return -1
