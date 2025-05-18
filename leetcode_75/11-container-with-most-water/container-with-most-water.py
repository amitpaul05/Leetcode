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
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            if height[l] < height[r]:
                max_area = max(max_area, (r - l) * height[l])
                l += 1
            else:
                max_area = max(max_area, (r - l) * height[r])
                r -= 1
        return max_area