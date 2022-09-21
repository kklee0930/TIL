## Django 개발 환경 설정 가이드

### 💻가상환경 생성 / 실행

#### 1. 프로젝트 디렉토리 생성

```bash
$mkdir test
$cd test
```

#### 2. 가상환경 생성

```bash
$python -m venv test-venv
```

#### 3. 가상환경 실행 / 종료

```bash
$source test-venv/Scripts/activate
# 혹은
$source ./activate

# 종료
$deactivate
```

<br>

### 💻Django LTS 버전 설치

#### 1. 가상환경 실행

```bash
$cd test
$source ./activate
```

#### 2. Django 설치

```bash
$pip install django==3.2.13
```
