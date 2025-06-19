class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # length=len(nums)
        # sol=[1]*length
        # pre = 1
        # post = 1
        # for i in range(length):
        #     sol[i] *= pre
        #     pre = pre*nums[i]
        #     sol[length-i-1] *= post
        #     post = post*nums[length-i-1]
        # return(sol)


        res = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]

        right = 1
        for r in reversed(range(len(nums))):
            res[r] *= right

            right *= nums[r]
        
        return res
