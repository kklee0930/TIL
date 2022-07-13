#두 번째로 큰 수를 찾아라.
numbers = [0, 20, 100, 40]
max = numbers[0]
second_max = numbers[0]

for i in numbers:
    if max < i:
        second_max = max
        max = i
    elif i < max and second_max < i:
        second_max = i   
print(second_max)
print(max)
