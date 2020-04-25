# 작업 분할 

현재의 backend branch안에서 

branch 2개를 나누고

backend branch로 merge,

master branch로 merge 하는 방식으로 해볼려고함.

<br>

1. 원격저장소 가져오기

   ```bash
   git clone https/github.com/gyunggyung/AiBetweenUs
   ```

2. 백엔드 브랜치로 checkout

   ```bash
   // 원격 브랜치 목록 확인
   git branch -r
   
   // backend branch로 checkout
   git checkout -t origin/backend
   ```

3. 백엔드 브랜치안에서 각자 브랜치 만들기

   ```bash
   git checkout -b <branch_name>
   
   // ex) 맞춤법 검사기 브랜치 만들기
   ex) git checkout -b spell checker
   ```

4. 작업후 백엔드 브랜치에서 merge

   ```bash
   // backend 브랜치로 checkout
   git checkout backend
   
   // 작업한 브랜치 merge
   git merge <branch_name>
   ```

5. 백엔드 브랜치에 푸쉬

   ```bash
   git push origin backend
   ```

6. 참고

   ```tex
   A가 작업후 백엔드 브랜치에 먼저 push하면
   
   B는 이전 백엔드 브랜치에서 작업 중이었으므로
   
   B의 작업 완료후 PUSH과정에서 오류가남(대략 pull을 먼저 하라는 내용)
   
   에서 두가지 정도 상황이 있을것으로 생각
   	1. B는 pull을 하여 최신 백엔드 브랜치로 업데이트하여 다시 push함 -끝-
   	2. B는 pull과정에서 A와 같은 파일을 수정하였기 때문에 pull에서 충돌, 수동으로 해야함?
   ```

   

