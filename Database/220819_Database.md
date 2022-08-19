💻CASE
특정 상황에서 데이터를 변환하여 활용할 수 있음
ELSE를 생략하는 경우 NULL값이 지정됨
데이터를 분류하여 출력한다

```SQL
--단순조회
SELCT id, gender
FROM healthcare
LIMIT 5;

--성별 1(남자), 2(여자)
SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
    END AS 성별
FROM healthcare
LIMIT 5;

--흡연(smoking)
SELECT DISTINCT smoking
FROM healthcare;

SELECT
    id,
    smoking,
    CASE
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '헤비스모커'
        ELSE '무응답'
    END
FROM healthcare
LIMIT 50;

--나이에 따라서 구분
--청소년(~18), 청년(~40), 중장년(~90)
SELECT
    last_name,
    first_name,
    age,
    CASE
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 40 THEN '청년'
        WHEN age <= 90 THEN '중장년'
        ELSE '노년'
    END
FROM healthcare
LIMIT 50;
```

💻서브쿼리(SUBQUERY)

`특정한 값을 메인 쿼리에 반환하여 활용`하는 것이다.
실제 테이블에 없는 기준을 이용한 검색이 가능하다.
서브쿼리는 소괄호로 감싸서
쉽게 말해서하나의 쿼리가 소괄호안에 들어가는 것이다!

- 단일행 서브쿼리
  서브쿼리의 결과가 0 또는 1개인 경우
  검색 결과가 딱 하나만 나올 때이다.
  주로 집계함수를 활용할 때 이러한 결과가 도출된다.

users에서 가장 나이가 작은 사람의 수는?

```SQL
-- 이런 식으로 야매로도 머리를 잘 굴리면 할 수는 있다
SELECT age, COUNT(*)
FROM healthcare
GROUP BY age
ORDER BY age;

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
SELECT COUNT(*)
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
    COUNT(*)
FROM USERS
WHERE country = (SELECT country
FROM users
WHERE last_name = '유' AND first_name = '은정');
```

전체 인원의 평균 연봉, 평균 나이를 출력해보자.

```SQL
SELECT COUNT(*), AVG(balance), AVG(age)
FROM users;

-- SELECT 문에서의 서브쿼리는 어떻게 활용할까?
SELECT
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉
FROM users;
```

- 다중행 서브쿼리

users에서 이은정과 같은 지역에 사는 사람의 수는?

```SQL
SELECT COUNT(*)
FROM users
WHERE country IN (SELECT country
FROM users
WHERE last_name = '유' AND first_name = '은정');
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
WHERE (last_name, age) IN (
    SELECT
        last_name,
        MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;
```
