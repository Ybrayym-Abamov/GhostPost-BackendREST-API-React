from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from django.utils import dateformat

from api.models import BoastsRoasts


class BoastsRoastsSerializer(ModelSerializer):
    score = SerializerMethodField(method_name='calculate_score')
    posted_time = SerializerMethodField(method_name='calculate_posted_time')

    class Meta:
        model = BoastsRoasts
        fields = [
            'id',
            'boolean',
            'body',
            'upvotes',
            'downvotes',
            'score',
            'posted_time'
        ]

    def calculate_score(self, instance):
        return (instance.upvotes - instance.downvotes)

    def calculate_posted_time(self, instance):
        return (dateformat.format(instance.datetime, 'g: i A M d, Y'))


class UpvoteSerializer(ModelSerializer):
    class Meta:
        model = BoastsRoasts
        fields = [
            'upvotes'
        ]


class DownvoteSerializer(ModelSerializer):
    class Meta:
        model = BoastsRoasts
        fields = [
            'downvotes'
        ]
