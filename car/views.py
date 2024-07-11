from rest_framework.views import APIView
from rest_framework import status
from .models import Car
from .serializers import CarSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class GetAllCarsAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCarAPIView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "incorrect data"}, status=status.HTTP_400_BAD_REQUEST)


class DeleteCarAPIView(APIView):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        if car:
            car.delete()
            return Response({"message": "car is deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "incorrect id"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateCarAPIView(APIView):
    def put(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "car is updated"}, status=status.HTTP_202_ACCEPTED)
        return Response({"message": "id or given data is incorrect"}, status=status.HTTP_400_BAD_REQUEST)


class CarDetailAPIView(APIView):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        if car:
            serializer = CarSerializer(car)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "incorrect id"}, status=status.HTTP_400_BAD_REQUEST)
