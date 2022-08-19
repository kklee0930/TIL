💻문자열 함수
SUBSTR(문자열, start, length): 문자열 자르기

시작 인덱스는 1, 마지막 인덱스는 -1

TRIM(문자열), LTRIM, RTRIM: 문자열의 공백을 제거한다
LENGTH(문자열): 문자열 길이
REPLACE(문자열, 패턴, 변경값): 패턴에 일치하는 부분을 변경
UPPER(문자열), LOWER(문자열): 문자열을 대문자, 소문자로 변경시켜준다.
||: 문자열 합치기(concatenation)

💻숫자 함수
ABS(숫자): 절대 값
SIGN(): 부호를 나타냄
MOD(숫자1, 숫자2): 숫자1을 숫자2로 나눈 나머지
CEIL, FLOOR, ROUND: 올림, 내림, 반올림
POWER(숫자1, 숫자2): 숫자1의 숫자2 제곱

💻GROUP BY

- SELECT문의 optional 절
- 행 집합에서 요약 행 집합을 만든다.
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만든다.
- 지정된 컬럼의 값이 같은 행들로 묶는다.
- 집계함수와 함꼐 활용되었을 때 의미가 있다.
- 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨진다.

```SQL
-- 성별 갯수
SELECT COUNT(*)
FROM users
GROUP BY last_name;

-- GROUP BY에서 활용하는 컬럼을 제외하고는 집계함수를 쓰시오
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;
```

GROUP BY 는 결과가 정렬되지 않는다.
정렬해서 출력하고 싶으면 ORDER BY를 사용하자.

💻쿼리문 실행 및 작성 순서

작성순서는
SELECT => FROM => WHERE => GROUP BY => HAVING => ORDER BY => LIMIT => OFFSET

실행 순서는
FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY

💻ALTER TABLE

1. 테이블 이름 변경
2. 새로운 column 추가
3. column 이름 수정 (new in sqlite 3.25.0)
4. column 삭제 (new in sqlite 3.35.0)

```SQL
-- 1. 테이블 이름 변경
ALTER TABLE table_name
RENAME TO new_name;

-- 2. 새로운 컬럼 추가
ALTER TABLE table_name
ADD COLUMN column_definition;

-- 3. 컬럼 이름 수정
ALTER TABLE table_name;
RENAME COLUMN current_name TO new_name;

-- 4. 컬럼 삭제
ALTER TABLE table_name;
DROP COLUMN column_name;
```
