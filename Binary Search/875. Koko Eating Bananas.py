class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """ Binary Search: O(n * logm)
            n = len(piles) 
            m = max(piles)
        - Binary Search to find min speed k within range (1, max(piles)) -> O(logm)
        - Everytime we try k, we test if total_time <= h once again -> O(n)
        """
        l, r = 1, max(piles)    # k search range: min speed 1, max speed = largest pile
        res = r                 # worse case: need max speed to eat the biggest pile

        while l <= r:
            mid = (l + r) // 2

            total_time = 0
            for p in piles:
                # ceil, not floor: speed = 3, need 2h to finish 5 piles, not 1
                total_time += math.ceil(p / mid)
            
            # if satisfy, update res and try smaller speed to minimize k
            if total_time <= h:
                res = mid
                r = mid - 1     # search smaller k if possible
            else:
                l = mid + 1     # else, search larger k
        
        return res              # return min valid speed