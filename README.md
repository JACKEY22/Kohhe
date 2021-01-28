# Kohhe

### stack 
- tool : pycharm,
- develop : python, django, javascript
- deploy : vultr, docker, portainer, mariadb, nginx, gunicorn

### 장고 기본적인 Workflow

-   1.model - database 설계
-   2.view  - 사용자의 요청을 처리
-   3.template - 사용자에게 보여줄 화면



### what I learned
- 자동로그인

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
- 보안
    장고에서 가본으로 제공하는 장식자 @login_required를 사용해 뷰 처리전 
    사용자의 로그인 여부를 확인할 수 있음 (각 뷰의 함수 수정 번거러움을 덜어줌)
    
    다른 사용자 정보에 접근을 막기위해 장식자를 만들어 사용
    ```
    def login_ownership_required(func):
        def decorated(request, *args, **kwargs):
            target_user = User.objects.get(pk=kwargs['pk'])
            if not target_user == request.user:
                return HttpResponseForbidden()
            return func(request, *args, **kwargs)
    return decorated
    ```
    
    장고 시크릿키를 분리해서 관리 (배포)
    ```
    import os, environ
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )
    # reading .env file
    environ.Env.read_env(
        env_file=os.path.join(BASE_DIR, '.env')
    )
    SECRET_KEY = env('SECRET_KEY')
    ```

- 반응형
    미디어쿼리를 사용 화면의 너비가 500px이하로 작아지면 글자의 크기를 12px
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




