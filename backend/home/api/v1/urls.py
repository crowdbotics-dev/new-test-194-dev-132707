from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    T1ViewSet,
    T2ViewSet,
    T1ViewSet,
    T2ViewSet,
    T1ViewSet,
    T2ViewSet,
    T1ViewSet,
    T2ViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("t1", T1ViewSet)
router.register("t2", T2ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
