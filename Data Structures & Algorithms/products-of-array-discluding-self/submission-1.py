class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        prod=1
        for i in range(len(nums)-1):
            prod=prod*nums[i]
            prefix.append(prod)
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            prefix[i] *= suffix
            suffix *= nums[i]
        return prefix
            


        