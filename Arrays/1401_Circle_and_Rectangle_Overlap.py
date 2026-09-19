class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        dx = xCenter - closest_x
        dy = yCenter - closest_y

        distance = dx * dx + dy * dy

        return distance <= radius * radius
