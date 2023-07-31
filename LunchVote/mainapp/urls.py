from django.urls import path
from .views import get_winner, get_all_winners

urlpatterns = [
    path('winner/', get_winner),
    path('winner/<str:date>', get_winner),
    path('winners/', get_all_winners),
]