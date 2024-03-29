### 💻딕셔너리(Dictionary)

1. 해시 테이블
2. 딕셔너리 기본 문법
3. 딕셔너리 메서드

딕셔너리는 공식적 명칭으로는 해시 테이블이라고 부른다.

딕셔너리의 key는 immutable하고 value는 mutable하다.

앞 부분에서 배웠듯이

```python
dict = {'a': 1, 'b': 2, 'c': 3}
dict['a'] = 2
print(dict) # {'a': 2, 'b': 2, 'c': 3}
```

이러한 방법으로 딕셔너리의 value를 변경할 수 있다(mutable).

딕셔너리는 `순서가 없지만 iterable하다`. 그게 큰 특징이다.

실제로 딕셔너리에서의 문자값은 Hash Function을 통해 해시라는 숫자 값으로 변경된다.

![](220728_Algorithm.assets/1200px-Hash_table_4_1_1_0_0_1_0_LL.svg.png)

[문자를 해시값으로 변경해보자](https://emn178.github.io/online-tools/sha256.html)

### 💻파이썬의 딕셔너리를 쓰는 이유?

사실 딕셔너리에는 키-값을 저장하기 위해 사용하는 이유도 있지만 그것보다 훨씬, 매우 큰 장점이 있다.

딕셔너리는 속도 측면에서 굉장한 효율성을 지닌다.

해시함수와 해시 테이블을 이용하기 때문에 `삽입,삭제,수정,조회 연산의 속도가 "리스트"보다 빠르다.`

Hash function을 이용한 `해시값 덕분에 위치를 바로 즉각적`으로 찾을 수 있다.

그렇기 때문에

- `get item`
- `insert item`
- `update item`
- `delete item`
- `search item`

과 같은 딕셔너리의 연산은 모두 `시간복잡도가 O(1)`이다!

### 💻그렇다면 딕셔너리를 언제 사용해야 할까?

1. 리스트를 사용하기 힘든 경우

2. 데이터에 대한 빠른 접근 탐색이 필요한 경우

3. 현실 세계의 대부분의 데이터를 다룰 경우

### 💻기본적인 딕셔너리 사용법

삽입 및 수정

```python
a = {
    'name': 'kyle',
    'gender': 'male',
    'address': 'Seoul,
}

a['job'] = 'coach' # 해당하는 키가 없으면 새로 생성하여 삽입, 존재하면 재정의.
del a['address'] # 키로 해당 key-value 제거
```

```python
# 딕셔너리의 또 다른 활용법

# 리스트안의 각 개별 원소의 갯수를 구하시오.
scores = ['A','B','C','D','A','B']

counter = {
    'A':0,
    'B':0,
    'C':0,
    'D':0
}

for score in scores:
    counter[score] += 1
```

```python
# Counter를 사용하면 리스트의 각 원소의 갯수를 쉽게 도출할 수 있다.
from collections import Counter

scores = ['A','B','C','D','A','B']

my_counter = Counter(scores)
print(my_counter)
```

삭제

`dict.pop(key)`: 딕셔너리에서도 pop(key)를 키에 해당하는 값을 지울 수 있다.

```python
a = {
    'name': 'kyle',
    'gender': 'male',
    'address': 'Seoul,
}
b = a.pop('name') # name의 key를 가진 것을 삭제한다.
print(b) # 삭제된 요소를 출력할 수도 있다.

a.pop('age') # 없는 요소를 삭제하려고 하면 KeyError가 발생한다.
```

조회

`dict.get(key)`
`dict[key]`

```python
a = {
    'name': 'kyle',
    'gender': 'male',
    'address': 'Seoul,
}
age = a.get('age', 29) # 해당 키 값이존재하지 않다면 29로 정의해준다.
print(age)
```

### 💻딕셔너리의 메서드

딕셔너리는 non-sequence 자료형이나, iterable하게는 만들 수 있다.

1. keys()

```python
john = {
    'name': 'john',
    'role': 'ceo'
}

# 반복문을 사용해서 key나 value를 출력
for elem in john:
    print(elem) # name, role

for elem in john:
    print(john[elem]) # john, ceo

# 반복문을 사용하지 않고 메서드를 사용하여 key나 value를 출력
print(john.keys()) # name, role
print(john.values()) #john, ceo
# 엄연히 말하면 type이 dict_keys 와 dict_values이나 사실상 리스트에서 사용 가능한 메서드와 함수를 모두 사용할 수 있으므로 리스트로 봐도 무방하다.

```

2. values()

```python
a = {
    'name': 'john',
    'gender': 'male',
    'address': 'Seoul
}

print(a.values())

```

3. items()

```python
john = {
    'name': 'john',
    'role': 'ceo'
}

print(john.items()) # 리스트 안의 튜플로 출력된다(dict_items() 타입). [('name', 'john'), ('role', 'ceo')]

for k, v in john.items():
    print(key, value)
```
