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

A: 2대 이상의 컴퓨터가 메시지를 보내고 받기 위해서는 서로를 특정할 수 있어야 하는데, IP(Internet Protocol) 주소로 서로를 특정한다. 이 주소는 구분 된 네 개의 숫자로 이루어져 있다. 하지만 이러한 IP 주소는 숫자로 이루어져있기 때문에 사람이 기억하기 어렵다는 단점이 존재하는데 사람이 기억하기 쉽게 IP 주소를 도메인 이름으로 변환하여 사용한다. 예로 구글의 IP 주소는 `173.194.121.32`이고 도메인 이름은 `google.com`이다.

2. 클라이언트와 서버는 무엇일까요?

A: 사용자가 사용하는 스마트폰, 컴퓨터와 같은 인터넷에 연결된 사용자 측면에서의 도구, 인터페이스를 `클라이언트`, 웹사이트, 사잍, 앱을 저장하는 컴퓨터를 `서버`라고 칭한다. 사용자가 웹사이트를 방문 할 때, 클라이언트가 서버에 요청을 보내고, 서버에서는 요청을 받아 응답을 클라이언트에게 전달한다. 클라이언트는 서버의 응답으로부터 웹사이트 파일을 받아 브라우저를 활용해서 웹사이트를 보여준다.

3. 정적 웹사이트와 동적 웹사이트의 차이점은 무엇일까요? Django는 무엇을 위한 도구인가요?

4. HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요?

5. 프레임워크는 무엇일까요?
