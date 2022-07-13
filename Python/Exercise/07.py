'''주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
min() 함수 사용 금지'''

numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100] # -60
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -100

min = []
for i in numbers:
    if min == []:
        min.append(i)
    elif min[0] >= i:
        min.pop()
        min.append(i)
print(min[0])