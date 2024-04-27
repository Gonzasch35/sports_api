from rest_framework import routers
from .api import TeamViewSet, PlayerViewSet

router = routers.DefaultRouter()

router.register('api/team', TeamViewSet, 'team')
router.register('api/player', PlayerViewSet, 'player')

urlpatterns = router.urls