from django.urls import path, include
from .views import (AmbassadorAPIView, ProductGenericAPIView, 
    LinkAPIView, OrderAPIView)

urlpatterns = [
    path('', include('common.urls')),
    path('ambassadors', AmbassadorAPIView.as_view()),   # http://localhost:8000/api/admin/ambassadors

    path('products', ProductGenericAPIView.as_view()), # http://localhost:8000/api/admin/products
    path('products/<str:pk>', ProductGenericAPIView.as_view()), # http://localhost:8000/api/admin/products/2

    path('users/<str:pk>/links', LinkAPIView.as_view()), # http://localhost:8000/api/admin/users/3/links

    path('orders', OrderAPIView.as_view()), # http://localhost:8000/api/admin/orders
]


