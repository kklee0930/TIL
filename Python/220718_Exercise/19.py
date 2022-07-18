'''양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지'''

#1
number = input()
print(len(number))

#2 
number = input()
number = list(map(int, number))
print(len(number))

#3
number = int(input())
cnt = 0
while number != 0:
    number //= 10
    cnt += 1
    
print(cnt)

#4 로그로도 풀 수 있다.
import math
number = 123
print(int(math.log(number, 10)) + 1)