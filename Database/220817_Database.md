💻SQlite 환경설정

💻SQL
UPDATE
C: INSERT
R: SELECT
U: UPDATE
D: DELETE

💻WHERE

```SQL
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 데이터 추가
.mode csv
-- 같은 디렉토리에 있는 users.csv 파일을 users 파일로 받아오기
.import users.csv users

-- 30세 이상인 사람들 모두 출력
SELECT * FROM users WHERE age >= 30;

-- 30세 이상인 사람들의 이름
SELECT first_name FROM users WHERE age >= 30;

-- 30세 이상의 사람들의 이름 3명만
SELECT first_name FROM users WHERE age >= 30 LIMIT 3;

-- 30세 이상이고 성이 김인 사람의 나이와 이름만 출력
SELECT age, first_name FROM users WHERE age >= 30 AND last_name = '김';
```

💻WHERE절에서 사용할 수 있는 연산자

1. 비교연산자: =, <=, >=, <, > 등 숫자 혹은 문자 값의 대/소, 동일 여부를 확인하는 연산자

2. 논리연산자

- AND: 앞에 있는 조건과 뒤에 오는 조건이 모두 참인 경우

- OR: 앞의 조건이나 뒤의 조건이 참인 경우

- NOT: 뒤에 오는 조건의 결과를 반대로

⛔주의!

```SQL
-- "키가 175" 이거나 "키가 183이면서 몸무게가 80"인 사람
WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80
-- 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80
```

💻그 밖에 SQL에서 사용할 수 있는 연산자
BETWEEN 값1 AND 값2
IN(값1,)
LIKE
IS NULL/IS NOT NULL

부정연산자

- 같지않다
- ~와 같지 않다.
- ~보다 크지않다

💻SQLite Aggregate Functions(집계함수)

- Aggregate function(집계함수)

값 집합에 대한 계산을 수행하고 단일 값을 반환(그 중의 하나가 우리가 사용했던 COUNT 이다!)

- COUNT: 그룹의 항목 수를 가져옴
- AVG: 그룹의 평균 값을 가져옴
- MAX: 그룹의 최대 값을 가져옴
- MIN: 그룹의 최소 값을 가져옴
- SUM: 그룹의 합을 가져옴

```SQL
-- 30세 이상인 사람들의 수
SELECT COUNT(*) FROM users WHERE age >= 30;

-- 전체 중에 가장 작은 나이
SELECT MIN(age) FROM users;

-- 이씨 중에 가장 작은 나이
SELECT MIN(age) FROM users WHERE last_name = '이';

-- 이씨 중에 가장 작은 나이를 가진 사람의 이름과 계좌잔고
SELECT MIN(age), first_name, balance FROM users WHERE last_name = '이';

-- 계좌 잔액(balance)이 가장 높은 사람과 그 액수를 조회
SELECT first_name, MAX(balance) FROM users;

-- 나이가 30 이상인 사람들의 평균 계좌잔고
SELECT AVG(balance) FROM users WHERE age >= 30;
```

💻LIKE
패턴을 찾기 위해 사용하는 명령어
패턴 일치를 기반으로 데이터를 조회하는 방법

와일드 카드
`SELECT * FROM table_name WHERE column LIKE pattern`

와일드카드 사용 예시:

2%: 2로 시작하는 문자열

%2: 2로 끝나는 문자열

%2%: 중간에 2가 들어가는 문자열

`_2%`: 두번째 문자가 2인 문자열

`1___`: 첫번째 문자가 1이고 길이가 4인 문자열

`2_%_% / 2__%`: 2로 시작하고 적어도 길이가 3인 문자열

```SQL
-- 테이블에서 지역 번호가 02인 사람만 조회
SELECT * FROM users WHERE phone LIKE '02-%';

-- 테이블에서 이름이 준으로 끝나는 사람만 조회
SELECT * FROM users WHERE first_name LIKE '%준';

-- 테이블에서 중간 번호가 5114인 사람만 조회
SELECT * FROM users WHERE phone LIKE '%-5114-%';
```

💻ORDER BY

ORDER BY는 오름차순과 내림차순을 기억하자. 쉽게 말해 데이터를 그냥 정렬(sort)하는 것이다.

SELECT 문에 추가하여 사용

조회 결과 집합을 정렬

정렬 순서를 위한 2개의 keyword를 제공한다.

- ASC: 오름차순(default)
- DESC: 내림차순

```SQL
-- 나이 오름차순으로 10개 데이터 추출(default가 오름차순이기 때문에 ASC 안적어도 됨)
SELECT * FROM users ORDER BY age ASC LIMIT 10;

-- 나이, 성 순으로 오름차순
SELECT * FROM users ORDER BY age, last_name LIMIT 10;

-- 계좌 잔액 순 내림차순
SELECT * FROM users ORDER BY balance DESC LIMIT 10;

-- 계좌 잔액 내림차순, 성 오름차순으로 출력
SELECT * FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;
```
