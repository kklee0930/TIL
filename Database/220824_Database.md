### 💻ORM(Object Relational Mapping)

> 매핑(mapping)이란 하나의 값을 다른 값으로 대응시키는 것을 말한다. 한자로는 사상(寫像)이라고 한다. '맵핑'이 아니라 '매핑'이 올바른 표기법이다. 매핑은 지도를 뜻하는 맵(map)에서 나온 말이다. 지도에 표시한 정보가 현실 세계와 1:1로 대응하듯이, 매핑을 통해 하나의 값을 다른 값으로 1:1 대응시키는 것을 말한다. 네임서버는 도메인 이름을 IP 주소로 매핑시키는 역할을 한다. 컴퓨터의 기억장치를 각각의 루틴이나 데이터 영역에 할당하는 것도 매핑의 일종이다.

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술이다.

파이썬에는 SQLAlchemy, peewee 등 라이브러리가 있으며 Django 프레임워크에서는 내장 Django DRM을 활용한다.

즉 객체(Object)로 DB를 조작하는 것이다. 프로그래밍 언어와 DB를 연동시킨다고 생각하자!

`Genre.objects.all()` == `SELECT * FROM Genre;`

- 모델 설계 및 반영

1. 클래스를 생성하여 내가 원하는 DB의 구조를 만든다.

```python
# models.Model이라는 내부 클래스를 상속 받는다.
class Genre(models.Model): # Genre가 클래스
    name = models.CharField(max_length = 30) # name이 속성(name TEXT)

class Artist(models.Model):
    name = models.CharField(max_length = 30)
    debut = models.DateField()
```

2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 자동 생성한다.

```bash

```

3. DB에 migrate한다.

### 💻Migration이란?

- Model에 생긴 변화를 DB에 반영하기 위한 방법

- 마이그레이션 파일을 만들어 DB 스키마를 반영한다.

- 명령어:

  - makemigrations: 마이그레이션 파일 생성

  - migrate: 마이그레이션을 DB에 반영

🌟만약에 모델에 변경사항이 생긴다면 어떻게 해야할까?

makemigrations

migrate

하자!

🍯Migrate 살펴보기

```sql
BEGIN;
--
-- Create model Genre
--
CREATE TABLE 'db_genre' (
    'id' integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name' varchar(30) NOT NULL
);

COMMIT;
```

### 💻환경설정

[환경설정 참고링크](https://github.com/kdt-hphk/DB-ORM)

### 💻데이터베이스 조작(Database API)

### 💻ORM 기본 조작

- Create

```python
# 1. create 메서드 활용
Genre.objects.create(name = '발라드')
```
