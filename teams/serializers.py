from rest_framework import serializers
from .models import Team, Player, Match, Fixture


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):

    team_player = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'image', 'team_player']

class MatchSerializer(serializers.ModelSerializer):

    local = serializers.SlugRelatedField(slug_field='name', queryset=Team.objects.all())
    visitante = serializers.SlugRelatedField(slug_field='name', queryset=Team.objects.all())

    class Meta:
        model = Match
        fields = '__all__'

class FixtureSerializer(serializers.ModelSerializer):
    
    match_fixture = MatchSerializer(many=True, read_only=True)
    

    class Meta:
        model = Fixture
        fields = ['id', 'name', 'match_fixture']
