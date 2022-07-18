'''> 문자열 word가 주어질 때, 해당 문자열에서 `a` 가 처음으로 등장하는 위치(index)를 출력해주세요.
`a` 가 없는 경우에는 `-1`을 출력해주세요.
`**find()` `index()` 메서드 사용 금지**
>'''
word = 'apple'
index = 0
for i in word:
    if i == 'a':
        print(index)
        break
    else:
        index += 1
else:
    print(-1)
    
#혹은
for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        break
    
#additional problem

'''문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
find() index() 메서드 사용 금지'''

input = 'HappyHacking'
index = 0
for i in input:
    if i == 'a':
        print(index)
    index += 1