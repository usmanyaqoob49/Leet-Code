class Solution(object):
    def nearestValidPoint(self, x, y, points):
        # set min_dist = some high number        
        min_dist = 10000000000

        # Set impossible idx
        idx = -5

        # loop through, check if point is valid and keep the idx if the dist is lower than
        # current min_dist
        for i in range(0,len(points)):
            if points[i][0] == x or points[i][1] == y:
                min_check = abs(x - points[i][0]) + abs(y - points[i][1])
                if min_check < min_dist:
                    min_dist = min_check
                    idx = i

        # Return idx as -1 if no valid points or idx if there were. 
        if idx == -5:
            return -1
        else:
            return idx