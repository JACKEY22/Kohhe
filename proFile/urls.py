from django.urls import path

from proFile.views import ProfileCreateView, ProfileUpdateView

app_name = 'profile'

urlpatterns=[

    path('create/', ProfileCreateView.as_view(), name="create"),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name="update"),

]