from django.conf.urls import url
from .views import UserSignUpApIView,GetUserListView

urlpatterns = [
    url('signup', UserSignUpApIView.as_view()),
    url('getUserList',GetUserListView.as_view())
]