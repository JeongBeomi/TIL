# 1. what_is_Github?
### 1-1. 버전관리
- 처음 생성부터 변경사항만 저장하고 최종 원본을 남긴다.
- git commit message : 변경이유
- git은 백업 복구 협업을 위한 버전 관리 프로그램중 하나.
- 기본적으로 snapshot 방식, 용량이 커지면 delta 방식으로 전환.
### 1-2. 분산
- 중앙 집중식 버전 관리(SVN) : 각 버전 파일이 중앙에 모여 있음.
- 분산 버전 관리(git) : 버전 파일이 각자에게 분산되어 있어 복구 쉬움.
### 1-3. Git vs Github
- git : 분산 버전 관리 프로그램
- github : git 기반의 저장소 서비스
- 개인 컴퓨터에서 git을 활용해 수정하고, 이것을 github에 올리면 모두가 공유할 수 있다.
### 1-4. local 저장소
![local](https://user-images.githubusercontent.com/109258397/179398979-35e483a1-cc55-4608-831e-7881ef72f457.png)
### 1-5. 원격 저장소
- 등록
```bash
git remote add origin <주소>
#remote(원격 저장소)에 origin이라는 이름으로 <주소>라는 주소의 원격 저장소를 add(추가)한다
```
- 조회
```bash
$ git remote -v
origin  <주소> (fetch)
origin  <주소> (push)
# add를 이용해 추가했던 원격 저장소의 이름과 주소를 출력
```
- 삭제
```bash
$ git remote rm origin
$ git remote remove origin
# remote(원격 저장소)와의 연결을 rm(remove, 삭제) 한다. 로컬과 원격 저장소의 연결을 끊는 것 삭제가 아님.
```
### 1-6. .gitignore
- .gitignore 작성 목록
  1. 민감한 정보가 담긴 파일(전화번호, 계좌번호, API KEY, 비밀번호 등)
  2. OS에 활용되는 파일
  3. IDE(pycharm) 혹은 Texteditor(vscode)등에서 활용되는 파일
  4. 개발 언어 혹은 프레임워크에서 사용되는 파일 (가상환경:venv/, __pycache__/)
- 작성 시 주의 사항
  1. 이름은 .gitignore
  2. .git폴더와 동일한 위치에 생성.
  3. 제외 하고 싶은 파일은 반드시 git add 전에 .gitigore에 작성.(git add를 먼저 하게되면 버전 관리 대상이 되어 이후에 .gitignore에 작성해도 무시되지 않고 계속 버전 관리 대상으로 인식됩니다.)
- .gitignore 작성 도움 사이트