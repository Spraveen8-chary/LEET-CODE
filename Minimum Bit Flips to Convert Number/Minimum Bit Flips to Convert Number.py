class Solution:
    def minBitFlips(self,start:int, goal:int)->int:
        return bin(start^goal).count('1')

test = Solution()
print(test.minBitFlips(start=10, goal=7))
print(test.minBitFlips(start=4, goal=5))
