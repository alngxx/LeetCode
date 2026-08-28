class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """ Simple Binary Search: O(log n)
        1. If arr[mid] > arr[mid + 1]: peak is mid, or left mid
        2. Else arr[mid] < arr[mid + 1]: peak is right of mid
        3. Since we keep narrow down to find peak in between l..r every step
        4. When l == r, it's peak
        """
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l