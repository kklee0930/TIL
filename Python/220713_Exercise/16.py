'''문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
모음 : a, e, i, o, u
**count() 사용 금지**'''

word = 'apple'
count = 0
for i in word:   
    if i in 'aeiou':
        count += 1
    #진짜 무식한 방법...    
    # if 'a' == i or 'e' == i or 'i' == i or 'o' == i or 'u' == i:
    #     count += 1
print(count)