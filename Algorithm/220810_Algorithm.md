💻그래프 탐색 알고리즘

그래프 알고리즘의 핵심은 `관계성`이다. 관계가 중요한 데이터에 그래프를 적용하면 문제를 굉장히 편하게 풀 수 있다.

데이터와 데이터가 선으로 연결되어 있으면 모두 그래프라고 말할 수 있다.

🌟그래서 그래프 탐색 알고리즘이 무엇일까?

시작 노드에서 간선을 타고 이동할 수 있는 모든 노드을 찾는 알고리즘이다.

이러한 그래프의 탐색 알고리즘에는 크게 두 가지가 있다.

🍯그래프 탐색 알고리즘은 그래프 + 스택 + 큐를 모두 활용한다.

1. 깊이 우선 탐색 (DFS): 스택 + 그래프

사진

DFS는 내려갈 수 있는 노드까지 최대한으로 내려가며 탐색하는 방식이다.

2. 넓이 우선 탐색 (BFS): 큐 + 그래프

사진

BFS는 레벨에서 남아있는 노드가 있을경우 그 노드를 순차적으로 탐색한 후, 레벨에 탐색할 노드가 남이있지 않으면 더 깊은 레벨의 노드로 내려가 순차탐색을 반복한다.

쉽게 말해 일차적으로 인접해 있는 노드부터 먼저 탐색하는 방식이다. 옆에 있는 노드부터 탐색하는 방식이다.

🍯BFS는 주로 최단거리를 찾는 문제가 주어졌을 때 활용된다.

💻깊이우선탐색(DFS)

시작 노드으로부터 갈 수 있는 하위 노드까지 가장 깊게 탐색하고, 더 이상 갈 곳이 없다면 마지막 갈림길로 돌아와서 다른 노드을 탐색하며 결국 모든 노드을 방문하는 순회 방법

특징:
모든 노드을 방문할 때 유리하다. 경우의 수, 순열과 조합에서 많이 사용된다.

BFS에 비해 코드 구현이 간단하다.

단, 모든 노드를 방문할 필요가 없거나 최단 거리를 구하는 경우에는 BFS가 더 유리하다.

DFS를 하기 전에 일단 탐색을 진행할 그래프가 필요한데, 이전에 학습했던 것과 같이

1. 인접행렬

```python
graph = [
    [0,1,1,0,0,0,0],
    []
]
```

2. 인접 리스트

```python
graph = [
    [1,2],
    [0,3,4],
    [0,4,5],
    [1],
    [1,2,6],
    [2],
    [4]
]
```

두 가지 방식으로 표현이 가능하다. 인접 리스트가 더 효율적이기 때문에 인접 리스트를 주로 활용한다.

💻DFS의 동작과정

각 노드를 방문했는지 여부를 판별할 수 있는 리스트를 만든다.

```python
visited = [0] * n # 노드의 갯수 n만큼
```

DFS의 사이클

1. 현재 노드 방문처리

2. 인접한 모든 노드 확인

3. 방문하지 않은 인접 노드 이동

stack을 활용해서 방문한 노드는 모두 1 처리해줌

방문 순서: 0-1-3-4-2-5-6

💻DFS의 구현방식

💻DFS 문제풀이
[BOJ 바이러스]()