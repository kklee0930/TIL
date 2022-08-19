💻Database

- 데이터베이스는 체계화된 데이터의 모임

- 여러 사람이 공유/사용할 목적으로 통합 관리되는 정보의 집합

- 논리적으로 연관된 자료의 모음으로 그 내용을 도도화 구조함으로써 검색과 갱신의 효율화를 꾀한 것이다.

💻why use Database?

아래와 같은 장점들이 존재한다.

- 데이터 중복 최소화

- 데이터 무결성

- 데이터 일관성

- 데이터 독립성(물리적/논리적)

- 데이터 표준화

- 데이터 보안 유지

💻RDB(Relational Dababase)

관계형 데이터베이스란?:

서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형

키와 값들의 간단한 관계를 `표 형태로 정리한 데이터 베이스`

🍯RDB에서 주로 사용되는 용어들

스키마(schema): 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것
ex: age = int, name = text 과 같이 데이터의 형태, 관계와 같은 전반적인 명세를 기술한다.
이러한 틀을 만들어 놓는 것을 스키마라고 한다. 지식을 표상하는 구조. 즉 스키마는 데이터베이스의 구조를 정의하는 용어라고 생각하면 된다.

테이블(table): 스키마를 바탕으로 만들어지는 것이 바로 테이블이다. 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합이다.

가로줄: 행,row,record
세로줄: 열,column, field

행: 실제 데이터가 저장되는 형태

기본키(Primary Key): 각 행(레코드)의 고유 값
반드시 설정해야 하며, 데이터베이스 관리 및 고나계 설정 시 주요하게 활용 됨.
각 튜플에 할당되는 `고유한 값`이어야 한다. 절대로 중복이 발생하지 않는 고유한 값이다. 예를 들어 대한민국 국민은 주민번호, 군인은 군번, 학생은 학번이 각각의 기본키가 된다고 할 수 있겠다.

💻RDBMS

관계형 데이터베이스 관리 시스템

SQLite

서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스

구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용된다.

로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능하다.

💻SQL(Structured Query Language)

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- ㅁ냐ㅐㅇ러잳럼잳러ㅑㅐㅁㅈㄷ랴ㅓㅐㅁㅈㄷㄹ

SQL의 언어는 크게 DDL, DML, DCL 세 가지로 나뉜다.

DDL(Data Definition Language): 데이터 정의 언어
관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 (CREATE, DROP, ALTER)

DML(Data Manipulation Language): 데이터 조작 언어
데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어

DCL(Data Control Language)

💻CREATE

반드시 세미콜론을 마지막에 붙여줘야한다.

```SQL
CREATE TABLE classmates(
    id INTEGER PRIMARY KEY,
    NAME TEXT
);

.tables # 하면 테이블의 목록 조회가 가능하다.

.schema classmates # 하면 특정 테이블의 스키마 조회가 가능하다.

INSERT INTO classmates VALUES (1, '홍길동'); # 값 추가가 가능하다.

SELECT * FROM classmates; # 테이블의 데이터를 조회가 가능하다.

INSERT INTO classmates VALUES (2, '이동희'); # 다시 값 추가가 가능하다.

DROP TABLE classmates; # 테이블 삭제
```

💻필드 제약 조건

- NOT NULL: NULL 값 입력 금지
- UNIQUE: 중복 값 입력 금지(NULL 값은 중복 입력 가능)
- PRIMARY KEY: 테이블에서 반드시 하나. NOT NULL + UNIQUE
- FOREIGN KEY: 외래키. 다른 테이블의 Key
- CHECK: 조건으로 설정된 값만 입력 허용
- DEFAULT: 기본 설정 값

```SQL
CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER DEFAULT 1 CHECK (0 < age)
);
```

💻CRUD
CREATE, READ, UPDATE, DELETE

- INSERT

"insert a single row into a table"
`INSERT INTO table_name (col1, col2) VALUES (val1, val2);`

classmates 테이블에 이름이 홍길동이고 나이가 23인 데이터를 넣어보자. SELECT문으로 확인해보자.

```SQL
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

SELECT \* FROM classmates;
```

INSERT 직접 해보기

- 홍길동 30 서울
- 김철수 30 제주
- 이호영 26 인천
- 박민희 29 대구
- 최혜영 28 전주

```SQL
INSERT INTO people VALUES
('홍길동', 30, '서울'),
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');
```

💻READ

- SELECT

"query data from a table"

- LIMIT

- WHERE

classmates 테이블에서 id,name 컬럼 값을 하나만 조회
`SELECT rowid, name FROM classmates LIMIT 1;`

2부터 시작(OFFSET 2)해서 하나 더 큰 값 하나만 조회(LIMIT 1)
`SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;` => 3 출력

조건에 해당되는 레코드만 출력
`SELECT * FROM classmates WHERE address = '서울';`

classmates 테이블 에서 age 를 중복없이 조회
`SELECT DISTINCT age FROM classmates;`

💻DELETE

조건에 해당하는 레코드만 삭제
`DELETE FROM classmates where rowid = 5;`

테이블 자체를 삭제
`DROP TABLE classmates;`

AUTO INCREMENT란
기존 값이 삭제되면 이어서 쓰는 것이 아니라 띄우고 이어진다.

```SQL
CREATE TABLE members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
)

INSERT INTO members VALUES
(1, '홍길동'),
(2, '김철수'),
(3, '이호영'),
(4, '박민희'),
(5, '최혜영');

Deelte FROM members where rowid = 5;
INSERT INTO members (name) VALUES ('고길동');
SELECT * FROM members
```

💻UPDATE

```SQL
UPDATE classmates SET address = '서울' WHERE rowid = 5;
SELECT * FROM classmates;
```
