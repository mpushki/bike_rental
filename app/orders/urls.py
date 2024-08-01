from django.urls import path
from .views import OrderHistoryAPIView, OrderCreateAPIView, ReturnBikeAPIView

urlpatterns = [
    path('create/', OrderCreateAPIView.as_view(), name='create_order'),
    path('return/<int:pk>', ReturnBikeAPIView.as_view(), name='return_bike'),
    path('history/', OrderHistoryAPIView.as_view(), name='history')
]
