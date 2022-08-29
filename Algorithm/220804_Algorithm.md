### 💻이중 리스트 순회

1. 이중 for문을 이용한 행 우선 순회

```python
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]

for i in range(3):
    for j in range(4):
        print(matrix[i][j], end=' ')
    print()

>> 1 2 3 4
>> 5 6 7 8
>> 9 0 1 2
```

🍯반드시 행 우선 순회를 할 필요는 없다! 다른 방식으로도 순회를 할 수 있다.

2. 이중 for문을 이요한 열 우선 순회

```python
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]

for i in range(4):
    for j in range(3):
        print(matrix[j][i], end=' ')
    print()

>> 1 5 9
>> 2 6 0
>> 3 7 1
>> 4 8 2
```

[참고] Pythonic한 방법으로 이중 리스트의 합 구하기

```python
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]

# 1. 일반적인 for문 활용하여 sum 구하기
total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        total += matrix[i][j]


🍯# 2. Pythonic한 방법 (map과 sum 활용하여 구하기)
total = sum(map(sum, matrix))

# 이런식으로 함수를 정의할 수도 있다.
def matrixSum(matrix):
    return sum(map(sum, matrix))
```

🌟이중 리스트에서 순회를 하기 위해서는 이중 range를 활용한 이중 for 문을 쓰는 것이 중요하다!

⛔이중 리스트는 이중 for 문을 돌기 때문에 시간복잡도가 O(N^2)이 된다.

행 우선 순회를 이용해 이차원 리스트의 최대값, 최소값을 구해보자.

```python
matrix = [
[0, 5, 3, 1],
[4, 6, 10, 8],
[9, -1, 1, 5]
]

max_val = 0

for i in range(3):
    for j in range(4):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
print(max_val)
```

```python
matrix = [
[0, 5, 3, 1],
[4, 6, 10, 8],
[9, -1, 1, 5]
]

min_val = 999999999

for i in range(3):
    for j in range(3):
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]

print(min_val)
```

🍯Pythonic한 방법으로도 구할 수 있다.

```python
matrix = [
    [0,5,3,1],
    [4,6,10,8],
    [9,-1,2,6]
]
min_ = min(map(min, matrix))
max_ = max(map(max, matrix))
```

[Jungol 937 : 리스트 3 - 형성평가 9](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4364&sca=pyc0)

<br>

### 💻전치(Transpose)

행렬의 행과 열을 서로 맞바꾸는 행위이다.

- 3 X 4 행렬이 transpose 과정을 거쳐 4 X 3 행렬이 된다.

- 2 X 3 행렬이 transpose 과정을 거쳐 3 X 2 행렬이 된다.

- 3 X 3 행렬이 transpose 과정을 거쳐 3 X 3 행렬이 된다.

전치 과정을 거친 행렬을 transpose matrix라고 한다!

```python
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]

transposed_matrix = [[0] * len(matrix) for _ in range(matrix[0])]

for i in range(4):
    for j in range(3):
        transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기

"""
transposed_matrix = [
[1, 5, 9],
[2, 6, 0],
[3, 7, 1],
[4, 8, 2]
]
"""
```

<br>

### 💻회전

이차원리스트를 회전시키는 유형의 문제도 존재한다. 예를 들어 90도 왼쪽으로 돌리기, 180도 돌리기, 이런 유형의 문제들이 출제 되기도 한다. 이런 문제는 어떻게 풀어야할까?

한번 스스로 고민해보자...
