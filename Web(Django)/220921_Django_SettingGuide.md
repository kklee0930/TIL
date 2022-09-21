## Django 개발 환경 설정 가이드

### 💻가상환경 생성 / 실행

#### 1. 프로젝트 디렉토리 생성

```bash
$ mkdir test
$ cd test
```

#### 2. 가상환경 생성

```bash
$ python -m venv test-venv
```

#### 3. 가상환경 실행 / 종료

```bash
$ source test-venv/Scripts/activate
# 혹은
$ source ./activate

# 종료
$ deactivate
```

<br>

### 💻Django LTS 버전 설치

#### 1. 가상환경 실행

```bash
$ cd test
$ source ./activate
```

#### 2. Django 설치

```bash
$ pip install django==3.2.13
```

<br>

### 💻Django 프로젝트 생성

#### 1. 가상환경 실행

```bash
$ cd test
$ source ./activate
```

#### 2. Django 프로젝트 생성

```bash
# $django-admin startproject 프로젝트명 디렉토리
$ django-admin startproject testpjt .
```

<br>

### 💻Django 실행

#### 1. 가상환경 실행

```bash
$ cd test
$ source ./activate
```

#### 2. Django 서버 실행

```bash
$ python manage.py runserver
```

#### 3. Django 서버 종료

```bash
$ ctrl+c
```

### 🌟220921\_실습 문제

1. IP와 도메인은 무엇일까요?

2. 클라이언트와 서버는 무엇일까요?

3. 정적 웹사이트와 동적 웹사이트의 차이점은 무엇일까요? Django는 무엇을 위한 도구인가요?

4. HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요?

5. 프레임워크는 무엇일까요?
