
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers

from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = []
    
    def create(self, request):
        todo = Todo.objects.create(
            title = self.request.data.get('title', ''), 
            description = self.request.data.get('description', ''), 
            user = request.user,
            )
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type='application/json')
