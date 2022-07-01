from django.db import router
from rest_framework import routers

from .viewsets import corpusViewSet

router = routers.DefaultRouter()
router.register(r'identify', corpusViewSet, 'corpus')

urlpatterns = router.urls