## branch in branch workflow

```bash
// show remote branch
git branch -r
```

<br>

```bash
// remote branch 가져오기
git checkout -t origin/<branch_name>
```

<br>

```bash
// branch 안에서 branch 생성
git checkout b <branch_in_branch>
```

<br>

```bash
// branch 안에서 branch 생성
git commit -m '#'

git checkout backend

git merge <branch_in_branch>

git push origin <branch>
```

<br>

## 브랜치 push할 때 원격 브랜치 최신버전과 충돌

```bash
// pull도 오류난다면 같은 파일이 수정되었을 가능성
// 이때는 수동 병합
git pull origin <branch>

git push origin <branch>
```

