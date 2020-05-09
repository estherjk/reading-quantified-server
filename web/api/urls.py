from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from accounts.views import UserViewSet
from books.views import BookViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'genres', GenreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API & token URLs for Simple JWT.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]
