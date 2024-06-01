from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.posts, name='posts'),
    path('about', views.abput, name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)