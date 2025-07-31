# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To count the maximum number of 1's in a given array.

# Approach
<!-- Describe your approach to solving the problem. -->
First I used sliding window technique, which was taking longer in execution.

instead if we use a temporary value it will be much easier.
actually it's not a sliding window problem at all.

# Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->




# Code
My initial approach(using sliding window):
```python3 []
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = left + 1
        count = 0
        if nums.count(1) == 0:
            return 0
        while left < len(nums) and right < len(nums):
            if nums[left] != 1:
                left += 1
                right = left + 1
            elif nums[right] != 1:
                count = max(count,right - left)
                left = right + 1
                right = left + 1
            elif nums[left] == 1 and nums[right] == 1:
                right += 1
        count = count = max(count,right - left)
        return count

```

My final approach to reduce execution time(using single loop):
```python3 []
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
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
        
```
