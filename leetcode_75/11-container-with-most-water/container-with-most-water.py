# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         start = 0
#         end = len(height) - 1
#         con = min(height[start],height[end]) * (end - start)
#         while start < end:
#             if height[start] > height[end]:
#                 temp = 1
#                 while height[end - temp] - height[end] < temp and temp < (end - start):
#                     temp += 1
#                 end = end - temp
#                 print(start, end, temp, min(height[start],height[end]))
#                 if min(height[start],height[end]) * (end - start) > con:
#                     con = min(height[start],height[end]) * (end - start)
#             else:
#                 temp = 1
#                 while height[start + temp] - height[start] < temp and temp < (end-start):
#                     temp += 1
#                 start = start + temp
#                 # print(start, end, min(height[start],height[end]))
#                 if min(height[start],height[end]) * (end - start) > con:
#                     con = min(height[start],height[end]) * (end - start)
            
#         return con


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1  
            else:
                r -= 1	
				
        return area