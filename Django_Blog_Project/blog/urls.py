from django.conf.urls import url
from .views import (CreateBlogAPIView ,
                    BlogListAPIView,
                    SelfBlogListAPIView,
                    UpdateBlogStatusAPIView)

urlpatterns = [
    url('createBlog', CreateBlogAPIView.as_view()),
    url('getBlogList', BlogListAPIView.as_view()),
    url('getSelfBlogList',SelfBlogListAPIView.as_view()),
    url('updateBlog/(?P<pk>.+)',UpdateBlogStatusAPIView.as_view())

    ]