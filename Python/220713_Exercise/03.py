'''1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

sum() 함수 사용 금지'''

n = 10

#while문
count = 1
result = 0
while count <= n:
    result += count
    count += 1
print(result)

#for문
result = 0
for count in range(1, n+1):
    result += count
print(result)