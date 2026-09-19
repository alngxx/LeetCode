class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """ Math: O(1), O(1)
        Check if the closest point of rectangle
        to circle center is inside circle area
        """
        # closest point (cx, cy) on rectangle to the circle center
        if xCenter < x1:
            cx = x1
        elif x1 <= xCenter <= x2:
            cx = xCenter
        else:
            cx = x2
        
        if yCenter < y1:
            cy = y1
        elif y1 <= yCenter <= y2:
            cy = yCenter
        else:
            cy = y2
        

        # check if the point is inside circle area
        # distance from center <= radius ** 2
        dx = cx - xCenter
        dy = cy - yCenter
        distance = dx ** 2 + dy ** 2
        if distance <= radius ** 2:
            return True
        return False