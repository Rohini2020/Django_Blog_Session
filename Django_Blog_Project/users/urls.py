from django.conf.urls import url
from .views import (UserSignUpApIView,
                    GetUserListView,
                    UserLoginAPIView )

urlpatterns = [
    url('signup', UserSignUpApIView.as_view()),
    url('getUserList',GetUserListView.as_view()),
    url('loginUser',UserLoginAPIView.as_view(),name="login")
]