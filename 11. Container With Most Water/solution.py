class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end, maxArea, temp = 0, len(height) - 1, 0, 0
        while start < end:
            if height[end] > height[start]:
                temp = height[start] * (end - start)
                if temp > maxArea:
                    maxArea = temp
                start += 1
            else:
                temp = height[end] * (end - start)
                if temp > maxArea:
                    maxArea = temp
                end -= 1
        return maxArea
