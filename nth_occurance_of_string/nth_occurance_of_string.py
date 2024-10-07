
class Solution():
    def nth_occurance_of_string(self:None, string:str, word:str, nth:int)->int:
        index = -1
        for _ in range(nth):
            index = string.find(word, index+1)
            if index == -1 : 
                return -1
        return index
    
sentence = "apple banana apple mango apple orange apple peach apple"
word = "apple"
print(Solution().nth_occurance_of_string(sentence,word, 1))
print(Solution().nth_occurance_of_string(sentence,word, 2))
print(Solution().nth_occurance_of_string(sentence,word, 3))
print(Solution().nth_occurance_of_string(sentence,word, 4))
print(Solution().nth_occurance_of_string(sentence,word, 5))

