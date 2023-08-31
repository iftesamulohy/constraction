from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class BaseViews(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model_name.objects.filter(is_deleted=False)
    @action(detail=True, methods=['post'])
    def soft_delete(self, request, pk=None):
        item = self.get_object()
        item.is_deleted = True
        item.save()
        return Response({"message": "Data deleted. But you can recover your data"})
    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        item = self.get_object()
        item.status = not item.status
        item.save()
        return Response({"message": "Status changed"})