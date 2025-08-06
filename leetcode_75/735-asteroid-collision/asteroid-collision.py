class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        # for index, i in enumerate(asteroids):
        #     if index == 0:
        #         stack.append(i)
        #         continue
            
        #     if i < 0 and stack[-1] > 0:
        #         if abs(i) == abs(asteroids[index-1]):
        #             stack.pop()
        #         elif abs(i) > asteroids[index-1]:
        #             stack.pop()
        #             stack.append(i)
        #             while len(stack)>1 and stack[-1] < 0 and stack[-2]>0:
        #                 if abs(stack[-1]) == abs(stack[-2]):
        #                     stack = stack[:-2]
        #                 elif abs(stack[-1]) < abs(stack[-2]):
        #                     stack = stack[:-1]
        #                 elif abs(stack[-1]) < abs(stack[-2]):
        #                     stack.pop(-2)
        #     else:
        #         stack.append(i)
        #     print(index, stack)
        # return stack

        res = []

        for a in asteroids:

            while res and a < 0 < res[-1]:
                if -a > res[-1]:
                    res.pop()
                    continue
                elif -a == res[-1]:
                    res.pop()
                break
            else:
                res.append(a)

        return res