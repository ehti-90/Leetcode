class Solution:
    def maxArea(self, height: List[int]) -> int:

    # brute force approach 
    
    #   n = len(height)
    #   max_water = 0

    #   for left in range(0,n):
        

    #     for right in range(left,n):
    #         width =   right - left
    #         hight = min(height[left], height[right])

    #         area = width * hight
            
    #         max_water = max(max_water, area)
    #   return max_water

        # optimal solution  O(n)
        left = 0
        right = len(height) - 1
        contain = 0

        while left < right:
            width = right - left
            max_height = min(height[left], height[right])
            area = width * max_height
            contain = max(contain, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return contain
