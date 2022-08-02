### 💻힙(Heap), 셋(Set)

일반적인 큐(Queue)는 순서를 기준으로 가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(First-In First-Out, 선입선출) 방식이다.

앞서 배웠던 Queue와 Stack은 모두 순서에 따라 데이터를 정렬하고 활용하는 데이터구조이다.

순서가 아닌 다른 기준으로는 데이터를 정렬, 활용할 수는 없을까?

### 💻힙(Heap)/우선순위 큐(Priority Queue)

우선순위 큐(Priority Queue)는 우선순위(중요도, 크기 등 순서 이외의 기준)를 기준으로 가장 우선순위가 높은 데이터가 가장 먼저 자료형을 빠져나가는 방식이다.

#### 🌟우선순위 큐(Priority Queue)가 그래서 무엇인가?

순서가 아닌 우선순위를 기준으로 가져올 요소를 결정(dequeue)하는 큐이다.

즉, 우선순위 큐에는

1. 가중치가 있는 데이터

2. 작업 스케줄링

3. 네트워크

의 특징이 있다.

#### 🌟우선순위 큐를 구현하는 방법에는

1. 배열(Array)

2. 연결 리스트(Linked List)

3. `힙(Heap)`

그렇다면 힙이 우선순위 큐인가?

- 우선순위 큐: 데이터를 조작하는 하나의 방식이다.

- 힙: 우선순위 큐로 활용할 수 있는 데이터구조이다.

따라서 우선순위 큐가 더 큰 개념이며 둘은 정확하게 같은 개념이라고 볼 수는 없다. 엄밀하게 말하면 힙이 우선순위 큐에 포함되는 부분집합의 개념이라고 생각하면 된다.

### 💻우선순위 큐 구현 별 시간 복잡도

![](220802_Algorithm.assets/2022-08-02%20225141.png)

![](220802_Algorithm.assets/time-complexity-examples.png)

### 💻힙(Heap)의 특징

힙이란 최대값 또는 최소값을 빠르게 찾아내도록 만들어진 데이터 구조이다.

힙은 `완전 이진 트리의 형태로 느슨한 정렬 상태를 지속적으로 유지`하며 힙 트리에서는 중복값을 허용하는 것이 특징이다.

힙의 가장 큰 특징이자 시그니쳐는 `대충 섞어서 굉장히 높은 효율을 내는 것`이 특징이다.

느슨한 정렬을 유지하는 것이 가장 큰 특징이다.

#### 🌟그래서 힙(Heap)을 언제 사용해야할까?

힙은 아래와 같은 상황에 활용된다.

1. 데이터가 지속적으로 정렬되어야 하는 경우

2. 데이터에 삽입/삭제가 빈번할 때

### 💻파이썬의 heapq모듈

힙을 코드로 직접 구현하는건 지금 상황으로는 무리이므로 파이썬의 모듈을 활용해보자!

힙은 기본적으로 `Minheap(최소 힙)`으로 구현되어 있다(가장 작은 값이 먼저 온다)

`Maxheap(최대 힙)`의 경우는 가장 큰 값이 리스트의 맨 앞에 오는 것이다.

🍯힙을 사용 시 삽입, 삭제, 수정, 조회 연산의 속도가 `리스트보다` 빠르다.
(배열, 연결리스트를 모두 힙으로 구현이 가능하다.)

따라서 리스트에 minheap을 적용시켜놓으면 리스트의 가장 맨 앞에 가장 작은 원소를 정렬해놓는다.

이것을 `느슨한 정렬`이라고 하며 내가 필요로 할 때 이러한 `최소값을 빠르게 뽑을 수 있도록 하기 위해서` 힙을 사용한다.

### 💻힙과 리스트의 비교

![](220802_Algorithm.assets/2022-08-02%202251411.png)

### 💻힙의 메서드

- `heapq.heapify()`: 힙을 생성한다.

- `heapq.heappop(heap)`: 힙에서의 minheap을 빼낸다. 뺀후에 minheap이 다시 인덱스 0자리로 돌아오는 느슨한 정렬이 이루어진다.

- `heapq.heappush(heap, item)`: 힙에 item을 삽입하고 다시 느슨한 정렬이 이루어진다.

힙을 통해서 입출력 결과를 확인해보자.

```python
import heapq

# 정렬되지 않은 데이터를 생성
numbers = [5,3,2,4,1]

# heapify는 destructive method이기 때문에 원본 데이터를 변형시킨다.
# 따라서 아래의 코드는 None이 출력된다.
numbers = heapq.heapify(numbers)
print(numbers) # None


numbers_2 = [5,3,2,4,1]
# 힙으로 만든다.
# heapq.heapify(iterable)
heapq.heapify(numbers_2)
print(numbers_2) # [1,3,2,4,5]
heapq.heappop(numbers_2) # 1이 빠져나온다.
print(numbers_2) # [2,3,5,4] 2가 min이므로 가장 앞으로 오게 정렬된다.
heapq.heappush(numbers_2, 10)
print(numbers_2) # [2,3,5,4,10]
heapq.heappush(numbers_2, 0)
print(numbers_2) # [0,3,2,4,10,5] 0이 min이므로 가장 앞으로 정렬되었다.

```

### BOJ 1927: 최소힙

![](220802_Algorithm.assets/2022-08-02%20112737.png)

```python
import heapq

heap = []

for _ in range(int(input())):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, n)
    elif len(heap) == 0 and n != 0:

    else:
        heapq.heappop(heap)
```

### 💻Set의 특징

셋은 기본적으로 수학에서의 '집합'을 나타내는 데이터 구조로 파이썬에서는 기본적으로 제공되는 데이터 구조이다.

셋의 메서드, 연산자에는 아래와 같은 것들이 있다.

- `.add()`

- `.remove()`

- `+(합)`

- `-(차)`

- `&(교)`

- `^(대칭자)`

### 💻Set은 언제 사용해야 할까?

Set은 아래와 같은 상황일 때 사용하는 것이 효율적이다.

1. 데이터 중복이 없어야 할 때 (고유값으로 이루어진 데이터가 필요할 때)

2. 정수가 아닌 데이터의 삽입/삭제/탐색이 빈번하게 필요할 때

### 💻Set의 연산 시간 복잡도

![](220802_Algorithm.assets/2022-08-02%202252537.png)

### boj 14425: 문자열 집합

```python

```

## References

https://adrianmejia.com/how-to-find-time-complexity-of-an-algorithm-code-big-o-notation/ (Time Complexity)
