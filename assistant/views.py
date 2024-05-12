from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from assistant.models import Assistant
from assistant.serializers import AssistantSerializer


class AddAssistant(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = AssistantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
class DeleteAssistant(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={"message": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class GetAssistantById(generics.RetrieveAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer

class UpdateAssistant(generics.RetrieveUpdateAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)