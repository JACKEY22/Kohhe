# Kohhe

### stack 
- tool : pycharm,
- develop : python, django, javascript
- deploy : vultr, docker, portainer, mariadb, nginx, gunicorn

### what I learned
mycode
```
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/create.html'
```
reference code(*After singing up, users' status is on)
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

responsive web
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




