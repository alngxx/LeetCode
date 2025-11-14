class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # number new flowers planted so far

        for i in range(len(flowerbed)):
            # Check if current position is empty
            if flowerbed[i] == 0:

                # Check left neighbor (out of bound or empty)
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)

                # Check right neighbor (out of bound or empty)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # If both neighbor are empty (True), can plant here
                if left_empty and right_empty:
                    flowerbed[i] = 1  # plant at position i
                    count += 1

        # If no. of able-to-plant flowers >= n -> True
        if count >= n:
            return True
        else:
            return False
