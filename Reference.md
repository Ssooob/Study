### 디렉토리 재설정
[링크](https://lvolz.tistory.com/23)
</br>

### 프로토콜
[출처](https://velog.io/@falling_star3/GitHub-git-add-commit-push-status-%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-%EC%9B%90%EA%B2%A9%EC%A0%80%EC%9E%A5%EC%86%8C%EB%A1%9C-%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)
1. git add 
    * 변경문 모아주는 작업
2. git status 
    * 디렉토리와 스테이징 영역 상태 확인
    </br>
    2-1. git rm --cached
        * add된 파일 취소
3. git commit -m "커밋내용"
</br>
    3-1. git commit --amend -m "수정된 메세지" 
        * 커밋 메세지 잘 못 작성했을 때 수정
4. git push -u origin master
    * 원격저장소에 업로드
    