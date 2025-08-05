Example grid:
```
grid = [[3,1,2,2],
        [1,4,4,4],
        [2,4,2,2],
        [2,5,2,2]]
```
# Step 1: What does `zip(*grid)` do?
It turns rows into columns.

Columns become:

```
(3, 1, 2, 2)
(1, 4, 4, 5)
(2, 4, 2, 2)
(2, 4, 2, 2)
```

# Step 2: `Counter(zip(*grid))` — what’s happening?
Count how many times each column appears.

Result:

```
(3,1,2,2): 1 time
(1,4,4,5): 1 time
(2,4,2,2): 2 times
```

# Step 3: `Counter(map(tuple, grid))` — what’s happening?
Count how many times each row appears (convert list → tuple so it can be counted).

Rows are:
```
(3,1,2,2)
(1,4,4,4)
(2,4,2,2)
(2,5,2,2)
```

Result:
```
Each row appears 1 time.
```

# Step 4: What does the `sum(tpse[t]*grid[t] for t in tpse)` do?
For each column tuple t, multiply:

```
Number of times column t appears (tpse[t]) × Number of times row t appears (grid[t])
```
Sum all those products.


# Step 5: Calculate for each `t`:
```
| `t`       | `tpse[t]` (columns) | `grid[t]` (rows) | Product | Explanation                    |
| --------- | ------------------- | ---------------- | ------- | ------------------------------ |
| (3,1,2,2) | 1                   | 1                | 1       | Column and row match once      |
| (1,4,4,5) | 1                   | 0                | 0       | No matching row                |
| (2,4,2,2) | 2                   | 1                | 2       | Column appears twice, row once |

```

Step 6: Final answer = 1 + 0 + 2 = 3

# Code
```python3 []
class Solution:                                
    def equalPairs(self, grid: List[List[int]]) -> int:

        tpse = Counter(zip(*grid))                  # <-- determine the transpose
                                                    #     and hash the rows

        grid = Counter(map(tuple,grid))             # <-- hash the rows of grid. (Note the tuple-map, so
                                                    #     we can compare apples w/ apples in next step.)

        return  sum(tpse[t]*grid[t] for t in tpse)  # <-- compute the number of identical pairs
```
