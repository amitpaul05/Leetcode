# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We need to find the longest subarray containing only 1s after flipping at most `k` zeros. A sliding window approach is ideal, where we expand the window to include more elements and shrink it when the number of zeros exceeds `k`.

# Approach
<!-- Describe your approach to solving the problem. -->
We use two pointers (`left` and `right`) to create a window over the input list. As we move the `right` pointer, we count the number of zeros encountered. Every time we see a zero, we decrement `k`. If `k` becomes negative, it means we've flipped more than allowed, so we move the `left` pointer forward to shrink the window until the number of flipped zeros is within the limit again. The size of the current valid window (`right - left + 1`) is tracked throughout.

# Complexity
- Time complexity:  
$$O(n)$$  
Each element is visited at most twice (once by `right`, once by `left`).

- Space complexity:  
$$O(1)$$  
Only a few pointers and counters are used.

# Debug Example
Input:  
```python
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

Step-by-step:

| Index (right) | nums[right] | k  | left | Window (nums[left:right+1]) | Window Length |
|---------------|-------------|----|------|------------------------------|----------------|
| 0             | 1           | 2  | 0    | [1]                          | 1              |
| 1             | 1           | 2  | 0    | [1, 1]                       | 2              |
| 2             | 1           | 2  | 0    | [1, 1, 1]                    | 3              |
| 3             | 0           | 1  | 0    | [1, 1, 1, 0]                 | 4              |
| 4             | 0           | 0  | 0    | [1, 1, 1, 0, 0]              | 5              |
| 5             | 0           | -1 | 0 → 1| [1, 1, 0, 0, 0]              | shrink         |
|               |             | -1 | 1 → 2| [1, 0, 0, 0]                 | shrink         |
|               |             | -1 | 2 → 3| [0, 0, 0]                    | shrink         |
|               |             | 0  | 3    |                              |                |
| 6             | 1           | 0  | 3    | [0, 0, 0, 1]                 | 4              |
| 7             | 1           | 0  | 3    | [0, 0, 0, 1, 1]              | 5              |
| 8             | 1           | 0  | 3    | [0, 0, 0, 1, 1, 1]           | 6              |
| 9             | 1           | 0  | 3    | [0, 0, 0, 1, 1, 1, 1]        | 7              |
| 10            | 0           | -1 | 3 → 4| [0, 0, 1, 1, 1, 1, 0]        | shrink         |
|               |             | -1 | 4 → 5| [0, 1, 1, 1, 1, 0]           | shrink         |
|               |             | -1 | 5 → 6| [1, 1, 1, 1, 0]              | shrink         |
|               |             | 0  | 6    |                              |                |

Maximum window size = **6**, between indices 3 and 8 → `[0, 0, 0, 1, 1, 1]` (after flips)

---

> Hit the Upvote button if you like the explaination.

---

# Code
```python3 []
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
      
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
        
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
      
        return right - left + 1
```





