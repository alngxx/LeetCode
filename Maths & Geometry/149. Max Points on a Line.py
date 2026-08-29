class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """ Hashmap: O(n²), O(n)
        1. Fix one point i (anchor point)
        2. For every j, compute the slope from i to j
        3. Points sharing same slope from i lie on same line to it
        4. Hashmap count number of points share slope to anchor, take the max
        5. Add 1 to include the anchor itself
        6. Update the global max
        """
        n = len(points)
        if n <= 2:
            return n
        
        res = 1
        for i in range(n):
            # empty hashmap for each anchor
            count = {}
            x1, y1 = points[i]
    
            # now, count the slope from other points to this anchor
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                
                count[slope] = count.get(slope, 0) + 1
            # edge case: i = last point, hashmap empty
            # after processing all other points
            # update max points on the same line with anchor i, plus i itself
            if count:
                res = max(res, max(count.values()) + 1)
        return res