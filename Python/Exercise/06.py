#get max
# numbers = [0, 20, 100, 40]
numbers = [-10, -100, -30]
max = float('-inf')
#max = -10 첫번째 값을 먼저 넣어놓고 시작하면 오히려 편하다!
for n in numbers:
    if max < n:
        max = n
print(max)