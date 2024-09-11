from typing import List

class Solution:
    def two_sum(self, nums:List[int], target:int)->List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+nums[j]==target:
                    return [i,j]
        return []
    
test = Solution()
print(test.two_sum(nums=[2,7,11,15], target=9))
print(test.two_sum(nums=[3,2,4], target=6))
print(test.two_sum(nums=[3,3], target=6))


