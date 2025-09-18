class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Intuition: Using two pointers i and j
        Loop through the array, whenever we found arr[j] != arr[i]
        Make all elements from arr[i] to arr[j] equally
        Finally, all unique elements place ordered at the beginning
        '''
        # i is the index of last unique element
        i = 0

        # Iterate from arr[1] -> arr[end]
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                # Increment i until i is the last unnique element
                i += 1
                nums[i] = nums[j]
        # k = i + 1: Number of unique elements, where i last unique element's index
        return i + 1
