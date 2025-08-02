# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Let's find the corner cases first.
- all elements are 1 -> return len(nums) - 1
- all elements are 0 -> return 0

# Approach
<!-- Describe your approach to solving the problem. -->
We go through the list and track how many `1`s are in a row.

We use two counters:
- `current_ones`: how many `1`s we are currently seeing.
- `previous_ones`: how many `1`s we saw just before the last `0`.

When we see a `0`, we pretend to delete it, and join the previous streak of `1`s and the current streak.  
We keep track of the best (longest) such joined streak using `max_ones`.

At the end, we also check one last time in case the list ends with `1`s.

# Debug Example  

```python
nums = [1, 1, 0, 1, 1, 1, 0, 1, 1]

# Index-by-index breakdown:

Index | num | current_ones | previous_ones | max_ones | Explanation
-------------------------------------------------------------------
0     | 1   | 1             | 0             | 0        | Start counting 1s
1     | 1   | 2             | 0             | 0        | Still counting
2     | 0   | 0             | 2             | 2        | Hit 0, simulate delete, max = 2
3     | 1   | 1             | 2             | 2        | New streak after 0
4     | 1   | 2             | 2             | 2        | Continue
5     | 1   | 3             | 2             | 2        | Continue
6     | 0   | 0             | 3             | 5        | Hit 0, simulate delete: 2+3 = 5
7     | 1   | 1             | 3             | 5        | New streak after 0
8     | 1   | 2             | 3             | 5        | Continue
```


# Complexity
- Time complexity: O(n)
We make a single pass through the list.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
We only use a few variables for tracking streaks and the result.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

---


> ***Please upvote if you like the approach***

---


# Code
```python3 []
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
```
