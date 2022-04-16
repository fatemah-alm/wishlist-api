from django.urls import URLPattern, path, include
from .views import ItemListView, ItemDetailView
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('items/', ItemListView.as_view(), name='api-list'),
    path('items/<int:id>', ItemDetailView.as_view(), name='api-detail'),
]

