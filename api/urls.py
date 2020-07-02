from django.conf.urls import include, url

from api.views import PostsViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'post', PostsViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls))
]
