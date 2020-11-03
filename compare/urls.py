from django.urls import path, include
from . import views
from .views import ItemListView

urlpatterns = [
    path('', ItemListView.as_view()),
    
    # path('', include('compare.urls'))
]
