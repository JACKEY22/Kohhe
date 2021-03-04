# 카페를 소개하는 게시판 

### app
account : 사용자 계정
profile : 사용자의 프로필 
article : 사용자가 작성하는 게시글
comment : 사용자가 게시글에 작성하는 댓글 
subscription : 사용자가 원하는 계정과 카페 계정을 팔로우 
shop : 카페 계정 

### model
account : Django에서 제공하는 User 모델
profile
```
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True, verbose_name='Status Message')
```
article
```
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True, verbose_name='제목')
    content = models.TextField(null=True, verbose_name='내용')
    image = models.ImageField(upload_to='article/', null=False, verbose_name='사진')
    created_at = models.DateField(auto_created=True, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, related_name='article', null=True, blank=True, verbose_name='카페')
```
comment
```
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
```
subscription
```
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='subscription', null=True)
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription_target', null=True)
    
    class Meta:
        unique_together = ('user', 'shop')
```
shop
```
class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop')
    name = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='shop/', null=True)
    notice = models.CharField(max_length=50)
    info = models.TextField(null=True)
    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name}'
```

### what I learned
- 반응형 웹 디자인(미디어쿼리)

    화면의 너비가 500px이하로 작아지면 글자의 크기를 12px
    ```
    @media screen and (max-width: 500px) {
        body {
            font-size:12px;
        }
    }
    ```





