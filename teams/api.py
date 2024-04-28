from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Team, Player, Match, Fixture
from .serializers import TeamSerializer, PlayerSerializer, MatchSerializer, FixtureSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlayerSerializer

class FixtureViewSet(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FixtureSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MatchSerializer

