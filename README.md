# Kohhe

### stack 
- tool : pycharm,
- develop : python, django, javascript
- deploy : vultr, docker, portainer, mariadb, nginx, gunicorn

### what I learned
- 자동로그인

    장고에서 제공하는 User(model) createview(view) UserCreationForm(form) 사용 - 
    사용자가 계정을 생성하고 다시 로그인해야 하는 상황 커스텀 필요
    ```
    class AccountCreateView(CreateView):
        model = User
        form_class = UserCreationForm
        success_url = reverse_lazy('account:login')
        template_name = 'account/create.html'
    ```
    authenticate함수와 login함수를 사용해 계정을 생성한 유저를 로그인
    상태로 자동으로 만들어줄 수 있다.
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
    장고에서 가본으로 제공하는 장식자 @ㅣogin_required를 사용해 뷰 처리전 
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




