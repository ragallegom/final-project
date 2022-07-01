from django.db import router
from rest_framework import routers

from .viewsets import NltkViewSet

router = routers.SimpleRouter()
router.register('corpus', NltkViewSet)

urlpatterns = router.urls