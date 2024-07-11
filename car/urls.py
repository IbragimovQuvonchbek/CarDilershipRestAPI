from django.urls import path
from .views import GetAllCarsAPIView, CreateCarAPIView, UpdateCarAPIView, DeleteCarAPIView, CarDetailAPIView

urlpatterns = [
    path('cars/', GetAllCarsAPIView.as_view(), name='get-all-cars'),
    path('car-create/', CreateCarAPIView.as_view(), name='create-car'),
    path('car-delete/<int:pk>/', DeleteCarAPIView.as_view(), name='delete-car'),
    path('car-update/<int:pk>/', UpdateCarAPIView.as_view(), name='update-car'),
    path('cars/<int:pk>/', CarDetailAPIView.as_view(), name="car-detail")
]
