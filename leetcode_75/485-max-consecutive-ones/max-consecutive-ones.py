class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # left = 0
        # right = left + 1
        # count = 0
        # if nums.count(1) == 0:
        #     return 0
        # while left < len(nums) and right < len(nums):
        #     if nums[left] != 1:
        #         left += 1
        #         right = left + 1
        #     elif nums[right] != 1:
        #         count = max(count,right - left)
        #         left = right + 1
        #         right = left + 1
        #     elif nums[left] == 1 and nums[right] == 1:
        #         right += 1
        # count = count = max(count,right - left)
        # return count

        current_max=0
        consecutive_sum=0 
        for i in nums:
            if i==1:
                consecutive_sum+=1
            else:
                if consecutive_sum>current_max:
                    current_max=consecutive_sum
                consecutive_sum=0
        if consecutive_sum>current_max:
            current_max=consecutive_sum
        return current_max


        