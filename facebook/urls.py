
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers
from post import views

router = routers.DefaultRouter()
router.register(r'post', views.PostView)
router.register(r'comment', views.CommentView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/', include('post.urls')),

]
