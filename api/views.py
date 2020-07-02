from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import BoastsRoastsSerializer, UpvoteSerializer, DownvoteSerializer
from api.models import BoastsRoasts

# https://simpleisbetterthancomplex.com/tips/2016/08/23/django-tip-13-f-expressions.html
from django.db.models import F


class PostsViewSet(ModelViewSet):
    serializer_class = BoastsRoastsSerializer
    queryset = BoastsRoasts.objects.all()

    @action(detail=True, methods=['post', 'get'])
    def upvote(self, request, *args, **kwargs):
        serializer = UpvoteSerializer(
            instance=self.get_object(),
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def downvote(self, request, *args, **kwargs):
        serializer = DownvoteSerializer(
            instance=self.get_object(),
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False)
    def boasts(self, request):
        boast_posts = BoastsRoasts.objects.filter(
            boast_or_roast='Boast').order_by('-datetime')
        page = self.paginate_queryset(boast_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(boast_posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roast_posts = BoastsRoasts.objects.filter(
            boast_or_roast="Roast").order_by('-datetime')
        page = self.paginate_queryset(roast_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(roast_posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def most_popular(self, request):
        vote_scores = BoastsRoasts.objects.all().order_by(
            -(F('upvotes') - F('downvotes')))
        page = self.paginate_queryset(vote_scores)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(vote_scores, many=True)
        return Response(serializer.data)
