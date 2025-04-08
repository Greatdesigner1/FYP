from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from students.views import SessionViewset, StudentsViewset


router = DefaultRouter()
router.register('', StudentsViewset)
router.register('session', SessionViewset)


urlpatterns = [
    path('', include(router.urls)),
]
