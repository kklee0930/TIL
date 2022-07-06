# Git Bash/Git 강의



## ❗Git Bash 명령어 정리

`mkdir foldername` : 폴더 생성 (make directory)

`pwd`: 현재 working direcory 표시 (print working directory)

`touch file` : 파일 생성

`cd ..`: 상위 폴더 이동 (change directory)

`rm -r foldername` : 폴더 삭제 (remove)

`rm file` : 파일 삭제

`ls` : 현재 디렉토리의 파일 목록 표시 (list)



## ❗Git

> 버전관리란: 컴퓨터 소프트웨어의 특정 상태

**Git** : 분선 버전 관리 시스템 / 형상 관리 도구

컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율



### Git 기초 흐름

**분산버전관리 시스템(DVCS)**

- 중앙에서 버전을 관리하고 파일을 받아서 사용
- 분산버전관리 시스템은 원격 저장소를 통해 저장/관리

**Git의 기본흐름**

1. 작업(수정)하고 [WORKING DIRECTORY : 1통]

2. 변경된 파일을 모아 (add) [STAGING AREA : 2통]

3. 버전으로 남긴다 (commit) [REPOSITORY : 3통]

`Working Directory` : 파일의 변경사항을 생성하는 곳

`Staging Area` : 버전으로 기록하기 위한 변경사항의 목록 (큰틀에서 게임의 테스트 서버. 최종적으로 커밋하기 전에 테스트를 위한 공간)

`Repository` : 커밋(버전)들이 최종적으로 기록되는 곳



`modified` : 파일이 수정된 상태(add 명령어 통해 staging area로)

`staged` : 수정한 파일을 곧 커밋할 것이라고 표시한 상태(commit 명령어로 저장소)

`committed` : 커밋이 된 상태



### Git 명령어 정리

`$git add <file>`: working directory 상의 변경 내용을 staging area에 추가하기 위해 사용

- untracked 상태의 파일을 staged 상태로 변경

`$git commit -m '<message>'` : staged 상태의 파일들을 커밋을 통해 버전으로 기록

- 나중에 되돌아가기 위해서 관리
- 파일 변경 사항들의 스냅샷이라고 생각하면 됨
- 파일들이 변경되었을 때 의도했던 행위를 기록한다고 생각하면 됨

`$git status` : Git 저장소에 있는 파일의 상태를 확인하기 위해서 활용

`$git log` : 현재 저장소에 기록된 커밋을 조회

- 다양한 옵션을 통해 로그를 조회할 수 있음
  - `$git log -1` : 최근 1개 커밋을 보여줘.
  - `$git log --oneline` : 커밋내역을 한 줄로 표시해줘
  - `$git log -2 --oneline` : 최근 2개 커밋내역을 두 줄로 표시해줘
  



# 로컬 저장소 만들기(연습)

## 1. 프로젝트 폴더 만들기

- 0706폴더 생성하기

## 2. 해당 폴더에서 Git 버전 관리 시작하기

```bash
$git init
```

- 주의! (master)라고 되어 있으면 상위 폴더를 생성하자.
- 명령어를 입력하게 되면 .git 폴더가 생성된다.

## 3. 작업

- 별도의 빈 파일 하나 생성
- status도 확인하기

## 4. 작업이 완료되면 커밋하기

- 커밋하고 log도 확인하기

## 5. 자유롭게 파일 만들고 수정하고 삭제하면서 커밋 3개 더 쌓아보기

- 수정하고 생성하는 작업이나 변경사항이 있어야만 add/commit 가능함



## ⛔주의사항

1. **(master) 있는 곳에서는 git init을 하지 않는다.**
2. **git 명령어를 입력할 때에는 항상 경로를 잘 보자.**
3. **명령어의 결과 영어를 잘 읽자.**
3. **모든 변경사항은 .git 폴더에 저장된다.**



# Git 실습

## 0. 사전 설정 (PC 최초 한번)

```bash
$git config --global user.name 'Github ID'
$git config --global user.email 'Github Email'
```

## 1. 바탕화면에 TIL 폴더를 만든다.

- TIL 폴더를 열어서 마크다운 정리 파일을 옮긴다.

## 2. TIL 폴더에 git 저장소를 만들어준다.

```bash
$git init
.
.
.(master) $
```

## 3. 커밋을 만든다.

```bash
$git status
On branch master

No commits yet
.
.

```

```bash
$git add .
$git commit -m '마크다운 정리'
$git log
```





