from rest_framework import serializers

from .models import User, Restaurant, Vote, Slot


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(required=False, many=True)

    class Meta:
        model = User
        fields = ['user', 'max_votes', 'votes']


class SlotSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(required=False, many=True)
    restaurant = RestaurantSerializer()

    class Meta:
        model = Slot
        fields = ['id', 'restaurant', 'votes', 'is_winner', 'date', 'votes_count', 'distinct_votes']