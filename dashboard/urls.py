from django.urls import path
from .views import home
from .views import list_items


urlpatterns = [
    path('', home),
    path('list_items/', list_items, name='list_items'),
]