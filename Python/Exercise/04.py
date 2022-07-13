'''1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.'''

n = 5

#while문
count = 1
result = 1
while count <= 5:
    result *= count
    count += 1
print(result)

#for문
result = 1
for count in range(1, n+1):
    result *= count
print(result)