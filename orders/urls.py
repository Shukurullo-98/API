from django.urls import path
from .views import OrderCreationListView, OrderDetailView, UpdateOrderStatus, UserOrdersView, UserOrderDetailView


urlpatterns = [
    path('', OrderCreationListView.as_view(), name='order-list'),
    path('<int:order_id>/', OrderDetailView.as_view(), name='order-detail'),
    path('update-status/<int:order_id>/', UpdateOrderStatus.as_view(), name='update-status'),
    path('user/<int:pk>/', UserOrdersView.as_view(), name='user-orders'),
    path('user/<int:user_id>/order/<int:order_id>/', UserOrderDetailView.as_view(), name='user-detail-view'),
]
