from django.shortcuts import render
from .models import student
from .serializers import StudentSerializer
from rest_framework import generics ,permissions,viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner==request.user

class studentviewset(viewsets.ModelViewSet):
    # queryset = student.objects.all()
    serializer_class = StudentSerializer
    permissions_classes=(IsOwner,)

    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            return student.objects.filter(owner=user)
        raise PermissionDenied()











# # Create your views here.
# class StudentList(generics.ListCreateAPIView):
#     queryset = student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = student.objects.all()
#     serializer_class = StudentSerializer
