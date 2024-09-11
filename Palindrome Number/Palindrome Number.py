class Solution:
    def isPalindrome(self, nums:int)->bool:
        reverse = 0
        temp = nums
        while nums:
            last = nums%10
            reverse = reverse*10 + last
            nums //= 10
        return reverse==temp

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(125))
print(Solution().isPalindrome(12321))

