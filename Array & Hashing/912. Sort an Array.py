class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge left and right sorted halves
        def merge(left, right):
            i, j = 0, 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            res.extend(left[i:])
            res.extend(right[j:])

            return res

        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            return merge(left, right)

        return mergesort(nums)
