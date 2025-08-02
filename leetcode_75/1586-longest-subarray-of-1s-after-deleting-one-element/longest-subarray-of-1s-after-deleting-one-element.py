class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(1) == len(nums):
            return len(nums) - 1
        elif nums.count(0) == len(nums):
            return 0
        max_ones = 0
        current_ones = 0
        previous_ones = 0

        for i in nums:
            if i == 1:
                current_ones += 1
            else:
                max_ones = max(max_ones, current_ones)
                current_ones = current_ones - previous_ones
                previous_ones = current_ones
        max_ones = max(max_ones, current_ones)
        return max_ones