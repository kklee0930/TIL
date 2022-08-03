### 💻이차원 리스트

이차원 리스트는 행렬을 표현한 자료형이지만 어렵게 생각할 필요는 없다.

코드 관점에서 보면 그저 리스트를 원소로 가지는 리스트일 뿐이다.

다시 정렬하면 행렬의 형태가 나온다.

```python
# 아래는
matrix = [[1,2,3],[4,5,6],[7,8,9]]

# 아래와 같다
# 보기 좋게 변경하면 결국 행렬의 형태가 나온다.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(matrix[0][0]) # 1
print(matrix[1][2]) # 5
print(matrix[2][0]) # 7
```

이차원 리스트를 직접 만들어보자.

```python
# 3 X 4 행렬을 만들어보자.

# 1. 아래와 같이 무식하게 직접 입력하여 만들 수 있지만, 만약에 100 X 100이라면 어떻게 만들까?
matrix1 = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

# 2. 반복문을 활용하여 작성 가능하다.
from pprint import pprint

matrix = []
for _ in range(100):
    matrix.append([0] * 100) # 원소 0이 100개가 포함된 리스트가 생성된다.

pprint(matrix) # 예쁘게 출력해보자.

# 3. 직접 row, column 정의하여 작성
from pprint import pprint

row = 4
column = 3

for _ in range(row):
    matrix.append([0] * column)

pprint(matrix)

# 4. list comprehension으로 작성

# 일반적인 방법이 아닌
for _ in range(10):
    matrix.append([0] * 10)

# list comprehension으로도 나타낼 수 있다.
matrix = [[0]* 10 for _ in range(10)]

# or
row = 10
column = 10
matrix = [[0] * row for _ in range(column)]

```

### 💻 [주의] 리스트 컴프리헨션 vs 리스트 곱셈 연산

조금 더 자세히 알아보자.

과연 아래의 matrix1과 matrix2의 값이 같을까?

```python
row = 3
column = 4

matrix1 = [[0] * column] * row

matrix2 = []
for _ in range(row):
    matrix2.append([0] * column)
```

출력해보면 결과는 같아 보이지만 인덱스를 활용해서 접근해보면 확실히 다르다는 것을 알 수 있다.

```python
matrix1[0][0] = 1
matrix2[0][0] = 1

print(matrix1)
print(matrix2)
```

#### ⛔결론은 리스트 곱셈 연산을 활용해서 이중리스트를 만들지 않는 것이 좋다. 인덱스를 활용하여 데이터를 조작하는 것이 불가능하기 때문이다.

이차원 리스트를 계속 연습해보자.

```python
# 3 X 3 크기의 입력을 받아보자.

matrix = []
for _ in range(3):
    line = list(map(int, input().split()))
    matrix.append(line)



'''
결과:
1 2 3
4 5 6
7 8 9
'''
```

#### ⛔list comprehension을 활용한 이차원리스트 생성이 헷갈리므로 반복을 통해 확실히 습득하자.

```python
row, column = map(int, input().split())

matrix = []
for _ in range(row):
    line = list(map(int, input().split()))
    matrix.append(list)

print(matrix)

# list comprehension으로 포현하면
matrix = [list(map(int, input().split())) for _ in range(row)]
```
