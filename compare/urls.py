from django.urls import path, include
from . import views
from .views import ItemListView, ItemCreateView, ItemUpdateView, ItemDetailView, DeleteItem
from . import views
urlpatterns = [
    path('', ItemListView.as_view(), name="list-home"),
    path('item/new/', ItemCreateView.as_view(), name="new-item" ),
    path('item/<int:pk>/update', ItemUpdateView.as_view(), name='update-item'),
    path('item/<int:pk>/',ItemDetailView.as_view(),name='detail-item'),
    path('item/<int:pk>/delete/', DeleteItem.as_view(), name='delete-item'),
    path('item/search/', views.search, name='search')
    # path('', include('compare.urls'))
]
