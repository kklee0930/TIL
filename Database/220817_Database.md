### 💻SQlite 환경설정 및 시작/파일생성

1. Table users 생성

```sql
-- 열 정의시: 열이름 타입 NULL여부
CREATE TABLE users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

```

2. csv파일 정보를 테이블에 적용하기

```SQL
sqlite> .mode csv
-- sqlite> .import 임포트할파일.csv 테이블명 (같은 디렉토리에 있는 CSV파일을 테이블로 생성한다.)
sqlite> .import users.csv users
sqlite> .tables

classmates examples users
```

### 💻SQL (지난 시간 RECAP)

가장 기본적인 4가지 SQL문에는 CREATE, READ, UPDATE, DELETE가 있다.

C: INSERT

```sql
-- 기본형: INSERT INTO 테이블 VALUES(값1,값2...)
-- INSERT INTO 테이블 (열1,열2...) VALUES(값1,값2...)
INSERT INTO users VALUES(1, '홍길동', 32)
INSERT INTO users (순번, 이름, 나이) VALUES(1, '홍길동', 32)
```

R: SELECT

```sql
-- 기본형: SELECT 특정 행 FROM 테이블
SELECT * FROM users
```

U: UPDATE

```sql
-- 기본형: UPDATE 테이블 SET 열 = '변경값' WHERE 조건
UPDATE users SET name = '홍길동' WHERE name = '김길동'
```

D: DELETE

```sql
-- 기본형: DELETE FROM 테이블 WHERE 조건
DELETE FROM users WHERE name = '홍길동'
```

### 💻WHERE

WHERE절은 테이블에서 특정 데이터를 조회하기 위해서 조건을 걸어주기 위해 사용된다.

```SQL
-- 30세 이상인 사람들 모두 출력
SELECT *
FROM users
WHERE age >= 30;

-- 30세 이상인 사람들의 이름
SELECT first_name
FROM users
WHERE age >= 30;

-- 30세 이상의 사람들의 이름 3명만
SELECT first_name
FROM users
WHERE age >= 30
LIMIT 3;

-- 30세 이상이고 성이 김인 사람의 나이와 이름만 출력
SELECT age, first_name
FROM users
WHERE age >= 30 AND last_name = '김';
```

### 💻WHERE절에서 사용할 수 있는 연산자

1. 비교연산자: =, <=, >=, <, > 등 숫자 혹은 문자 값의 대/소, 동일 여부를 확인하는 연산자

2. 논리연산자

- `AND`: 앞에 있는 조건과 뒤에 오는 조건이 모두 참인 경우

- `OR`: 앞의 조건이나 뒤의 조건이 참인 경우 (다수의 조건 중 하나만 참이라도 허용)

- `NOT`: 뒤에 오는 조건의 결과를 반대로

⛔주의!

```SQL
-- "키가 175" 이거나 "키가 183이면서 몸무게가 80"인 사람
WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80
-- 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80

```

왜 이렇게 다른 결과가 나오는 것일까?

이는 프로그래밍에서의 연산자 우선순위와 깊은 관계가 있다. 아래 링크에서 확인해보자.

- 연산자 우선순위:

  1. 괄호()

  2. NOT

  3. 비교연산자(<,>,<=,>=,=)

  4. AND

  5. OR

🍯[연산자 우선순위](http://www.tcpschool.com/codingmath/priority)

### 💻그 밖에 SQL에서 사용할 수 있는 연산자

- `BETWEEN 값1 AND 값2`: 값 <= 비교값 <= 값2

- `IN (값1, 값2, 값3....)`: 값이 목록 중의 값과 하나라도 일치하는지 확인

- `LIKE`: 비교 문자열과 형태가 일치하는지 확인. 와일드카드(%)와 함꼐 사용됨

- `IS NULL/IS NOT NULL`: NULL 여부를 확인할 때 사용. 항상 = 대신에 IS 사용해야함

- `부정연산자`

  같지않다: `!=, ^=, <>`

  ~와 같지 않다: `NOT 컬럼명 = 비교값`

  ~보다 크지않다: `NOT 컬럼명 > 비교값`

  ```SQL
  WHERE 컬럼명1 != 비교값1
  AND 컬럼명2 ^= 비교값2
  AND 컬럼명3 <> 비교값3
  AND NOT 컬럼명4 = 비교값4
  AND NOT 컬럼명5 > 비교값5;
  ```

### 💻SQLite Aggregate Functions(집계함수)

- Aggregate function(집계함수)

  값 `집합에 대한 계산`을 수행하고 단일 값을 반환(그 중의 하나가 우리가 사용했던 COUNT 이다!)

  - COUNT: 그룹의 항목 수를 가져옴

  - AVG: 그룹의 평균 값을 가져옴

  - MAX: 그룹의 최대 값을 가져옴

  - MIN: 그룹의 최소 값을 가져옴

  - SUM: 그룹의 합을 가져옴

```SQL
-- 30세 이상인 사람들의 수
SELECT COUNT(*)
FROM users
WHERE age >= 30;

-- 전체 중에 가장 작은 나이
SELECT MIN(age)
FROM users;

-- 이씨 중에 가장 작은 나이
SELECT MIN(age)
FROM users
WHERE last_name = '이';

-- 이씨 중에 가장 작은 나이를 가진 사람의 이름과 계좌잔고
SELECT MIN(age) AS min_age, first_name, balance
FROM users
WHERE last_name = '이' AND age = min_age;

-- 계좌 잔액(balance)이 가장 높은 사람과 그 액수를 조회
SELECT first_name, MAX(balance) AS max_bal
FROM users
WHERE balance = max_bal;

-- 나이가 30 이상인 사람들의 평균 계좌잔고
SELECT AVG(balance)
FROM users
WHERE age >= 30;
```

### 💻LIKE

패턴을 찾기 위해 사용하는 명령어이며 패턴 일치를 기반으로 데이터를 조회하는 방법이다.

- 와일드 카드

  기본형: `SELECT * FROM table_name WHERE column LIKE pattern`

- 와일드카드 사용 예시:

  - `2%`: 2로 시작하는 문자열

  - `%2`: 2로 끝나는 문자열

  - `%2%`: 중간에 2가 들어가는 문자열

  - `_2%`: 두번째 문자가 2인 문자열

  - `1___`: 첫번째 문자가 1이고 길이가 4인 문자열

  - `2_%_% / 2__%`: 2로 시작하고 적어도 길이가 3인 문자열

```SQL
-- 테이블에서 지역 번호가 02인 사람만 조회
SELECT *
FROM users
WHERE phone
LIKE '02-%';

-- 테이블에서 이름이 준으로 끝나는 사람만 조회
SELECT *
FROM users
WHERE first_name
LIKE '%준';

-- 테이블에서 중간 번호가 5114인 사람만 조회
SELECT *
FROM users
WHERE phone
LIKE '%-5114-%';
```

### 💻ORDER BY

ORDER BY는 오름차순과 내림차순을 기억하자. 쉽게 말해 데이터를 그냥 정렬(sort)하는 것이다.

ORDER BY는 SELECT 문에 추가하여 사용한다.

궁극적인 목적은 조회 결과 집합을 정렬하는 것이다.

- 정렬 순서를 위한 2개의 keyword를 제공한다.

  - `ASC`: 오름차순(default)

  - `DESC`: 내림차순

```SQL
-- 나이 오름차순으로 10개 데이터 추출(default가 오름차순이기 때문에 ASC 안적어도 됨)
SELECT *
FROM users
ORDER BY age ASC
LIMIT 10;

-- 나이, 성 순으로 오름차순
SELECT *
FROM users
ORDER BY age, last_name
LIMIT 10;

-- 계좌 잔액 순 내림차순
SELECT *
FROM users
ORDER BY balance DESC
LIMIT 10;

-- 계좌 잔액 내림차순, 성 오름차순으로 출력
SELECT *
FROM users
ORDER BY balance DESC, last_name ASC
LIMIT 10;
```
