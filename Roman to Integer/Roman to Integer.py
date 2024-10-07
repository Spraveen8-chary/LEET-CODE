class Solution:
    def roman_to_integer(self, roman:str)->int:
        numbers = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }

        total = 0
        prev = 0

        for i in reversed(roman):
            curr = numbers[i]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total

print(Solution().roman_to_integer("III"))
print(Solution().roman_to_integer("LVIII"))
