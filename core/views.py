from django.shortcuts import render
from rest_framework import pagination
from .serializers import *
from .models import *
from rest_framework.generics import *
from .pagination import MyPageNumberPagination
# Create your views here.



class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination