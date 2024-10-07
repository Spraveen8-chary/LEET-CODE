
def solution(sentence:str)->str:
    vowels = ['a', 'e', 'i','o' ,'u']
    count = 1
    result = ''
    for i in sentence:
        if i in vowels:
            result += count*"#"
            count += 1
            continue
        result += i
    return result

sentencs = "life is beautiful".lower()
print(solution(sentencs))

