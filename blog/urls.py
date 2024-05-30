from . import views
from django.urls import path

urlpatterns = [
    path('', views.posts, name='posts'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
