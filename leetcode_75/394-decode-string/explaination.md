# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
There are only 4 types of characters possible. 
- `[`,
- `]`,
- `digit`, and 
- `alphabet`

# Approach
<!-- Describe your approach to solving the problem. -->
if `[` then `->` curString and curNum will be added to stack and reset
if `]` then `->` prevString, and curString will be reset

try to decode remaining two types by your own

Debug example:
```
Code block

| Char  | Action                                                                                       | `stack`                             | `curNum` | `curString`                                                     |
| ----- | -------------------------------------------------------------------------------------------- | ----------------------------------- | -------- | --------------------------------------------------------------- |
| `'3'` | Digit → `curNum = 3`                                                                         | `[]`                                | `3`      | `''`                                                            |
| `'['` | Push `curString`, `curNum` → reset both                                                      | `['', 3]`                           | `0`      | `''`                                                            |
| `'z'` | Append to `curString`                                                                        | `['', 3]`                           | `0`      | `'z'`                                                           |
| `']'` | Pop 3, '' → `curString = '' + 3 * 'z'` = `'zzz'`                                             | `[]`                                | `0`      | `'zzz'`                                                         |
| `'2'` | Digit → `curNum = 2`                                                                         | `[]`                                | `2`      | `'zzz'`                                                         |
| `'['` | Push `curString`, `curNum` → reset                                                           | `['zzz', 2]`                        | `0`      | `''`                                                            |
| `'2'` | Digit → `curNum = 2`                                                                         | `['zzz', 2]`                        | `2`      | `''`                                                            |
| `'['` | Push `curString`, `curNum` → reset                                                           | `['zzz', 2, '', 2]`                 | `0`      | `''`                                                            |
| `'y'` | Append to `curString`                                                                        | `['zzz', 2, '', 2]`                 | `0`      | `'y'`                                                           |
| `']'` | Pop 2, '' → `curString = '' + 2 * 'y' = 'yy'`                                                | `['zzz', 2]`                        | `0`      | `'yy'`                                                          |
| `'p'` | Append to `curString`                                                                        | `['zzz', 2]`                        | `0`      | `'yyp'`                                                         |
| `'q'` | Append to `curString`                                                                        | `['zzz', 2]`                        | `0`      | `'yypq'`                                                        |
| `'4'` | Digit → `curNum = 4`                                                                         | `['zzz', 2]`                        | `4`      | `'yypq'`                                                        |
| `'['` | Push `curString`, `curNum` → reset                                                           | `['zzz', 2, 'yypq', 4]`             | `0`      | `''`                                                            |
| `'2'` | Digit → `curNum = 2`                                                                         | `['zzz', 2, 'yypq', 4]`             | `2`      | `''`                                                            |
| `'['` | Push `curString`, `curNum` → reset                                                           | `['zzz', 2, 'yypq', 4, '', 2]`      | `0`      | `''`                                                            |
| `'j'` | Append to `curString`                                                                        | `['zzz', 2, 'yypq', 4, '', 2]`      | `0`      | `'j'`                                                           |
| `'k'` | Append to `curString`                                                                        | `['zzz', 2, 'yypq', 4, '', 2]`      | `0`      | `'jk'`                                                          |
| `']'` | Pop 2, '' → `curString = '' + 2 * 'jk' = 'jkjk'`                                             | `['zzz', 2, 'yypq', 4]`             | `0`      | `'jkjk'`                                                        |
| `'e'` | Append to `curString`                                                                        | `['zzz', 2, 'yypq', 4]`             | `0`      | `'jkjke'`                                                       |
| `'1'` | Digit → `curNum = 1`                                                                         | `['zzz', 2, 'yypq', 4]`             | `1`      | `'jkjke'`                                                       |
| `'['` | Push `curString`, `curNum` → reset                                                           | `['zzz', 2, 'yypq', 4, 'jkjke', 1]` | `0`      | `''`                                                            |
| `'f'` | Append to `curString`                                                                        | `['zzz', 2, 'yypq', 4, 'jkjke', 1]` | `0`      | `'f'`                                                           |
| `']'` | Pop 1, 'jkjke' → `curString = 'jkjke' + 1 * 'f' = 'jkjkef'`                                  | `['zzz', 2, 'yypq', 4]`             | `0`      | `'jkjkef'`                                                      |
| `']'` | Pop 4, 'yypq' → `curString = 'yypq' + 4 * 'jkjkef'` = `'yypqjkjkefjkjkefjkjkefjkjkef'`       | `['zzz', 2]`                        | `0`      | `'yypqjkjkefjkjkefjkjkefjkjkef'`                                |
| `']'` | Pop 2, 'zzz' → `curString = 'zzz' + 2 * 'yypqjkjkef...'` = `'zzzyypqjkjkef...yypqjkjkef...'` | `[]`                                | `0`      | `'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkef'` |
| `'e'` | Append to `curString`                                                                        | `[]`                                | `0`      | `'...ef'`                                                       |
| `'f'` | Append to `curString`                                                                        | `[]`                                | `0`      | `'...eff'`                                                      |

```

# Complexity
- Time complexity: `O(n)`
<!-- Add your time complexity here, e.g. $$O(n)$$ -->


# Code
```python3 []

class Solution(object):
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():     # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

```
