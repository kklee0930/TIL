### 💻CASE

특정 상황에서 데이터를 `변환하여 활용할 수 있음`

ELSE를 생략하는 경우, NULL값이 지정됨

데이터를 `분류하여 출력한다`

```SQL
-- 기본형
SELECT 컬럼명
    CASE
        WHEN 조건식 THEN 식
        WHEN 조건식 THEN 식
        ELSE 식
    END
FROM 테이블명

--테이블에서 행을 5개까지 단순조회 해보자.
SELCT id, gender
FROM healthcare
LIMIT 5;

--테이블에서 성별 1(남자), 2(여자)
SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
    END AS 성별
FROM healthcare
LIMIT 5;

--테이블에서 흡연자(smoking)만 뽑아서 출력해보자.
SELECT DISTINCT smoking
FROM healthcare;

SELECT
    id,
    smoking,
    CASE -- CASE문을 활용하여
        WHEN smoking = 1 THEN '비흡연자' -- smoking = 1인 행을 비흡연자,
        WHEN smoking = 2 THEN '흡연자' -- 2인 행을 흡연자
        WHEN smoking = 3 THEN '헤비스모커' -- 3인 행을 헤비스모커로 출력
        ELSE '무응답' -- 그 외의 값은 무응답으로 출력
    END
FROM healthcare
LIMIT 50; -- 출력갯수를 50개로 제한

--나이에 따라서 구분
--청소년(~18), 청년(~40), 중장년(~90)
SELECT
    last_name,
    first_name,
    age,
    CASE -- CASE문 활용하여
        WHEN age <= 18 THEN '청소년' -- 18세 이하는 청소년,
        WHEN age <= 40 THEN '청년' -- 40세 이하는 청년
        WHEN age <= 90 THEN '중장년' -- 90세 이하는 중장년
        ELSE '노년' -- 그 외의 값은 노년으로 출력
    END
FROM healthcare
LIMIT 50;
```

### 💻서브쿼리(SUBQUERY)

서브쿼리는 쿼리 안의 쿼리로 생각하면 편하다. 이 때, 쿼리를 포함하는 상위의 쿼리를 `메인쿼리`라고 하고 포함되는 쿼리를 `서브쿼리`라고 칭한다.

서브쿼리란: `특정한 값을 메인 쿼리에 반환하여 활용`하는 것이다.

실제 테이블에 없는 기준을 이용한 검색이 가능하다. 주로 다른 테이블의 데이터를 조회하여 WHERE절을 통한 조건으로 활용하고 싶을 때 사용한다.

서브쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 컬럼을 모두 사용할 수 있다.

⛔하지만 그 반대로 메인쿼리가 서브쿼리의 컬럼은 사용할 수 없다.

### 💻단일행 서브쿼리

서브쿼리의 결과가 0개 또는 1개인 경우, 서브쿼리를 `단일행 서브쿼리`라고 한다.

주로 집계함수를 활용할 때 이러한 결과가 도출된다.

단일행 비교 연산자(=, <, >, <=, >=, <>)와 함께 사용된다.

users에서 가장 나이가 작은 사람의 수는?

```SQL
-- 이런 식으로 야매로도 머리를 잘 굴리면 할 수는 있다
SELECT age, COUNT(*)
FROM healthcare
GROUP BY age -- age별로 그룹화
ORDER BY age -- 오름차순으로 정렬하여
LIMIT 1; -- 가장 처음의 행(나이가 가장 작은 사람의 수)만 출력한다.

-- 하지만 서브쿼리를 사용한다면?

-- 서브쿼리
SELECT MIN(age)
FROM users;

-- 메인쿼리
SELECT COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);
```

users에서 평균 계좌 잔고보다 높은 사람의 수?

```SQL
-- 1. 먼저 평균계좌잔고 확인 코드를 작성해본다.(서브쿼리 작성)
SELECT AVG(balance)
FROM users;

-- 2. 메인쿼리 작성를 작성한다.
SELECT balance AS 평균_계좌_잔고, COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM healthcare);
```

users에서 유은정과 같은 지역에 사는 사람의 수는?

```SQL
-- 1. 먼저 유은정이 어디에 사는지 알아야한다.
SELECT
    country,
    last_name,
    first_name
FROM users
WHERE last_name = '유' AND first_name = '은정';

-- 2. 전체쿼리 작성
SELECT
    country AS 지역, COUNT(*)
FROM users
WHERE country = (
    SELECT country
    FROM users
    WHERE last_name = '유' AND first_name = '은정'
    );
```

전체 인원의 평균 연봉, 평균 나이를 출력해보자.

```SQL
SELECT COUNT(*) AS 총인원, AVG(balance) AS 평균연봉, AVG(age) AS 평균나이
FROM users;

-- SELECT 문에서의 서브쿼리는 어떻게 활용할까?
SELECT
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉
FROM users;
```

### 💻다중행 서브쿼리

단일행 서브쿼리와는 다르게 `서브쿼리의 결과가 2개 이상`인 경우, 이를 `다중행 서브쿼리`라고 한다.

단일행 서브쿼리는 단일행 비교연산자와 함께 사용되는 반면, 다중행 서브쿼리는 다중행 비교연산자와 함께 사용된다.

다중행 비교연산자에는 `IN, EXISTS` 등이 있다.

users에서 이은정과 같은 지역에 사는 사람의 수는?

```SQL
SELECT COUNT(*)
FROM users
WHERE country IN (SELECT country
FROM users
WHERE last_name = '이' AND first_name = '은정');
```

- 다중컬럼 서브쿼리

특정 성씨에서 가장 어린 사람들의 이름과 나이를 출력해보자.

```SQL
-- 특정 성씨에서 가장 적은 나이/사람 모두 출력
SELECT
    last_name,
    MIN(age)
FROM users
GROUP BY last_name;

SELECT
    last_name,
    first_name,
    age
FROM users
WHERE (last_name, age) IN ( -- 다중행 비교연산자인 IN을 활용하여 last_name과 age를 한번에 비교한다.
    SELECT
        last_name,
        MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;
```
