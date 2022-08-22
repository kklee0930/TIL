### 💻문자열 함수

- `SUBSTR(문자열, start, length)`: 문자열 자르기(시작 인덱스는 1, 마지막 인덱스는 -1)

- `TRIM(문자열), LTRIM, RTRIM`: 문자열의 공백을 제거한다

- `LENGTH(문자열)`: 문자열 길이

- `REPLACE(문자열, 패턴, 변경값)`: 패턴에 일치하는 부분을 변경

- `UPPER(문자열), LOWER(문자열)`: 문자열을 대문자, 소문자로 변경시켜준다.

- `||`: 문자열 합치기(concatenation)

### 💻숫자 함수

- `ABS(숫자)`: 절대 값

- `SIGN(숫자)`: 부호를 나타냄(양수 1, 음수 -1, 0, 0)

- `MOD(숫자1, 숫자2)`: 숫자1을 숫자2로 나눈 나머지

- `CEIL(숫자), FLOOR(숫자), ROUND(숫자)`: 올림, 내림, 반올림

- `POWER(숫자1, 숫자2)`: 숫자1의 숫자2 제곱

- `SQRT(숫자)`: 제곱근

### 💻GROUP BY

- "make a set of summary rows from a set of rows"

- 값 집단에 대한 계산을 실시하고 단일 값을 반환한다.

- 행 집합에서 요약 행 집합을 만든다.

- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만든다.

- 지정된 컬럼의 값이 같은 행들로 묶는다.

- 집계함수와 함께 사용되었을 때 의미가 있으며 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨진다.

```SQL
-- 기본형
SELECT *
FROM 테이블 이름
GROUP BY 컬럼1, 컬럼2;

-- 성별(last_name) 갯수
SELECT COUNT(*)
FROM users
GROUP BY last_name;

-- 각 last_name 별 갯수, 나이의 평균 출력
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;
```

⛔주의사항

GROUP BY절에 명시하지 않은 컬럼은 별도로 지정할 수 없다. 그룹마다 하나의 행을 출력하게 된다.

GROUP BY 는 결과가 정렬되지 않는다. 정렬해서 출력하고 싶으면 ORDER BY를 사용하자.

### 💻쿼리문 실행 및 작성 순서

- 작성순서는:

  SELECT => FROM => WHERE => GROUP BY => HAVING => ORDER BY => LIMIT => OFFSET

- 실행 순서는:

  FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY

### 💻HAVING

실행순서에 의해 집계함수는 WHERE절에는 사용할 수 없다 (WHERE로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞에 있기 때문이다).

따라서 GROUP BY를 통해 컬럼 별로 데이터를 집계한 후, 원하는 조건에 맞는 데이터를 HAVING절을 통해 추려내게 된다.

```SQL
-- 기본형
SELECT *
FROM 테이블이름
GROUP BY 컬럼1, 컬럼2
HAVING 그룹조건;
```

### 💻ALTER TABLE

ALTER TABLE은 테이블에 새로운 데이터를 삽입하거나 기존데이터를 삭제, 또는 수정 할 때 사용된다.

1. 테이블 이름 변경

   ```SQL
   -- 기본형
   ALTER TABLE 테이블이름
   RENAME TO 새로운이름;
   ```

2. 새로운 column 추가

   ```SQL
   -- 기본형
   ALTER TABLE 테이블이름
   ADD COLUMN 컬럼이름;
   ```

3. column 이름 수정 (new in sqlite 3.25.0)

   ```SQL
   -- 기본형
   ALTER TABLE 테이블이름
   RENAME COLUMN 기존테이블 TO 새로운이름;
   ```

4. column 삭제 (new in sqlite 3.35.0)

   ```SQL
   -- 기본형
   ALTER TABLE 테이블이름
   DROP COLUMN 컬럼이름;
   ```

🍯테이블을 생성하고 ALTER TABLE을 통해 값을 조작 및 추가 해보자.

- title과 content라는 컬럼을 지니는 articles 라는 이름의 table을 새롭게 만들어보자 (두 컬럼 모두 비어 있어서는 안되며, rowid를 사용한다).

  ```sql
  CREATE TABLE(
      title TEXT NOT NULL,
      content TEXT NOT NULL
  );
  ```

- articles 테이블에 값을 추가해보자(title은 '1번제목', content는 '1번내용').

  ```SQL
  INSERT
  INTO articles
  VALUES ('1번제목', '1번내용');
  ```

- 테이블의 이름을 변경해보자.

  ```SQL
  ALTER TABLE articles
  RENAME TO news;
  ```

- 테이블에 새로운 컬럼을 추가해보자.

  ```SQL
  -- 기본형
  ALTER TABLE 테이블이름
  ADD COLUMN 컬럼이름

  ALTER TABLE news
  ADD COLUMN new_col TEXT;
  ```
