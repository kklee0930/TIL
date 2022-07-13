'''주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.'''

word = 'apple'
reversed = ''
for i in word:
    reversed  = i + reversed
print(reversed)

#또는
reversed = word[::-1]
print(reversed)

#index 조작으로 풀기 (이 방법에 익숙해지자.)
box = ''
for i in range(len(word)):
    box += word[(len(word)-i-1)]
print(box)