# REST API

* [참고자료](https://meetup.toast.com/posts/92)



>#### 2) Stateless (무상태성)
>
>REST는 무상태성 성격을 갖습니다. 다시 말해 작업을 위한 상태정보를 따로 저장하고 관리하지 않습니다. 세션 정보나 쿠키정보를 별도로 저장하고 관리하지 않기 때문에 API 서버는 들어오는 요청만을 단순히 처리하면 됩니다. 때문에 서비스의 자유도가 높아지고 서버에서 불필요한 정보를 관리하지 않음으로써 `구현이 단순`해집니다.
>
>#### 5) Client - Server 구조
>
>REST 서버는 API 제공, 클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보)등을 직접 관리하는 구조로 각각의 역할이 확실히 구분되기 때문에 클라이언트와 서버에서 개발해야 할 내용이 명확해지고 `서로간 의존성`이 줄어들게 됩니다.
>
>
>
>REST API 설계 시 가장 중요한 항목은 다음의 2가지로 요약할 수 있습니다.
>**첫 번째,** `URI는 정보의 자원을 표현`해야 한다.
>**두 번째,** 자원에 대한 `행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현`한다.
>다른 것은 다 잊어도 위 내용은 꼭 기억하시길 바랍니다.



# spa

* [spa](http://devstory.ibksplatform.com/2017/08/spasigle-page-applications.html)
* [react spa](https://brunch.co.kr/@go-rani/4)