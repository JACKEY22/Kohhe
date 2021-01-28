# Kohhe

### stack 
- tool : pycharm,
- develop : python, django, javascript
- deploy : vultr, docker, portainer, mariadb, nginx, gunicorn

### what I learned
- 자동로그인

    장고에서 제공하는 User(model) createview(view) UserCreationForm(form) 사용
    사용자가 계정을 생성하고 다시 로그인해야 하는 상황 발생 
    ```
    class AccountCreateView(CreateView):
        model = User
        form_class = UserCreationForm
        success_url = reverse_lazy('account:login')
        template_name = 'account/create.html'
    ```
    form을 통해 데이터를 받아 authenticate함수와 login함수를 사용해 계정을 생성한 유저를 로그인
    상태로 자동으로 만들어준다.
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

- 반응형
    미디어쿼리를 사용 화면의 너비가 500px이하로 작아지면 글자의 크기를 12px
    ```
    @media screen and (max-width: 500px) {
        body {
            font-size:12px;
        }
    }
    ```
    how to keep the secret key
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
### Feedback
- after singing up, users don't need to log in
- like or recommend 
- comment update
- unlimited scroll paging
- bookmark cafe users frequently visit
- order and pay on website
- coupon

### URL : -- 




