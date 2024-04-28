from rest_framework import routers
from .api import TeamViewSet, PlayerViewSet, FixtureViewSet, MatchViewSet

router = routers.DefaultRouter()

router.register('api/team', TeamViewSet, 'team')
router.register('api/player', PlayerViewSet, 'player')
router.register('api/fixture', FixtureViewSet, 'fixture')
router.register('api/match', MatchViewSet, 'match')

urlpatterns = router.urls