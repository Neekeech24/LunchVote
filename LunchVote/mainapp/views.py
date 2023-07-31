import json
from datetime import datetime

from django.apps import apps
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Restaurant, Vote, Slot
from .serializers import UserSerializer, RestaurantSerializer, VoteSerializer, SlotSerializer


# Authorization views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def patch(self, request):
        pk = request.data["pk"]
        name = request.data["name"]
        if pk and name:
            try:
                r = Restaurant.objects.get(pk=pk)
                r.name = request.data["name"]
                r.save()
                return Response(200)
            except:
                return Response(404, {"message": f"No place for id {request.data['pk']} was found"})
        else:
            return Response(400, {"message": "No required data was provided"})


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

@api_view(['GET',])
def get_winner(request):
    if date := request.GET.get('date', None):
        date = datetime.strptime(date, "%Y-%m-%d")
    else:
        date = datetime.today()

    try:
        slot = Slot.objects.get(date=date, is_winner=True)
        serialized_data = SlotSerializer(slot)
        return Response(status=200, data=serialized_data.data)
    except Slot.DoesNotExist:
        return Response(status=400, data={'message': 'No winner found for that date'})


@api_view(['GET'])
def get_all_winners(request):
    filters = {"is_winner": True}
    if start_date := request.GET.get('start_date', None):
        filters.update({"date__gte": datetime.strptime(start_date, "%Y-%m-%d")})

    if end_date := request.GET.get('end_date', None):
        filters.update({"date__lte": datetime.strptime(end_date, "%Y-%m-%d")})

    winners = Slot.objects.filter(**filters)
    if winners:
        serialized_data = SlotSerializer(winners, many=True)
        return Response(status=200, data=serialized_data.data)
    else:
        return Response(status=400, data={"message": "No winners for selected period"})

