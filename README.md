# Kohhe

### stack 
- tool : pycharm,
- develop : python, django, javascript
- deploy : vultr, docker, mariadb,

### code
```
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/create.html'
```

### URL : -- 




