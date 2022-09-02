from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Food, FoodCategory
from .serializers import FoodSerializer, FoodListSerializer
from django.db.models import Prefetch




class FoodCategoryView(viewsets.ViewSet):
    
    serializer_class = FoodListSerializer

    def list(self, request):
        queryset = (
            FoodCategory
            .objects
            .prefetch_related(
                Prefetch(
                    'food',
                    queryset=Food.objects.filter(is_publish=True)))
            .order_by('pk'))

        serializer = FoodListSerializer(queryset, many=True)
        return Response(serializer.data)