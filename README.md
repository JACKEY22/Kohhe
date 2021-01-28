# Kohhe

### stack 
- tool : pycharm,
- develop : python, django, javascript
- deploy : vultr, docker, portainer, mariadb, nginx, gunicorn

### 장고 기본적인 Workflow

    1.model - database 설계
    2.view  - 사용자의 요청을 처리
    3.template - 사용자에게 보여줄 화면



### what I learned
- 자동로그인 함수(장고 제공)

    authenticate, login함수를 사용해 
    계정을 생성한 유저를 로그온 상태로 자동으로 만들어줄 수 있다.
    ```
    def signup(request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')
        else:
            form = UserForm()
        return render(request, 'common/signup.html', {'form': form})
    ```
    
- 장식자(파이썬 문법)

    view단 처리전 반복되는 로직을 구현 가능 - 코드 가독성
    
    요청을 보낸 유저와 해당 데이터의 소유자의 일치여부 확인 장식자
    ```
    def login_ownership_required(func):
        def decorated(request, *args, **kwargs):
            target_user = User.objects.get(pk=kwargs['pk'])
            if not target_user == request.user:
                return HttpResponseForbidden()
            return func(request, *args, **kwargs)
    return decorated
    ```
    class형 view의 decorator 사용법
    ```
    @method_decorator(decorator, 'get or post')
    class test():
    ```

- 반응형 웹 디자인(미디어쿼리)

    화면의 너비가 500px이하로 작아지면 글자의 크기를 12px
    ```
    @media screen and (max-width: 500px) {
        body {
            font-size:12px;
        }
    }
    ```
    
### Feedback
- after singing up, users don't need to log in
- like or recommend 
- comment update
- unlimited scroll paging
- bookmark cafe users frequently visit
- order and pay on website
- coupon

### URL : -- 




