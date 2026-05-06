from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    include(router.urls),
]

# Добавляем JWT эндпоинты вручную
from django.urls import path
urlpatterns += [
    path('v1/', include(router.urls)),
    path('v1/jwt/', include('rest_framework_simplejwt.urls')),
]
