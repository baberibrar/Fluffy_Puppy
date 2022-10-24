from .serializers import BreedSerializer, DogSerializer
from .models import Breed, Dog
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = BreedSerializer(queryset, many=True)
            return Response(
                {
                    "message": "List of all breeds",
                    "responsePayload": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request, *args, **kwargs):
        try:
            serializer = BreedSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Breed created successfully",
                        "responsePayload": serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {
                    "message": "Breed not created",
                    "responsePayload": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = Breed.objects.all()
            breed = get_object_or_404(queryset, pk=kwargs['pk'])
            serializer = BreedSerializer(breed)
            return Response(
                {
                    "message": "Breed retrieved successfully",
                    "responsePayload": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            queryset = Breed.objects.all()
            breed = get_object_or_404(queryset, pk=kwargs['pk'])
            serializer = BreedSerializer(breed, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Breed updated successfully",
                        "responsePayload": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                {
                    "message": "Breed not updated",
                    "responsePayload": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        try:
            queryset = Breed.objects.all()
            breed = get_object_or_404(queryset, pk=kwargs['pk'])
            breed.delete()
            return Response(
                {
                    "message": "Breed deleted successfully",
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = DogSerializer(queryset, many=True)
            return Response(
                {
                    "message": "List of all dogs",
                    "responsePayload": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request, *args, **kwargs):
        try:
            serializer = DogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Dog created successfully",
                        "responsePayload": serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {
                    "message": "Dog not created",
                    "responsePayload": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = Dog.objects.all()
            dog = get_object_or_404(queryset, pk=kwargs['pk'])
            serializer = DogSerializer(dog)
            return Response(
                {
                    "message": "Dog retrieved successfully",
                    "responsePayload": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            queryset = Dog.objects.all()
            dog = get_object_or_404(queryset, pk=kwargs['pk'])
            serializer = DogSerializer(dog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Dog updated successfully",
                        "responsePayload": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                {
                    "message": "Dog not updated",
                    "responsePayload": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        try:
            queryset = Dog.objects.all()
            dog = get_object_or_404(queryset, pk=kwargs['pk'])
            dog.delete()
            return Response(
                {
                    "message": "Dog deleted successfully",
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )
