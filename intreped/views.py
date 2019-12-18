from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from models.models import Users, Courses, User_courses, Badges, User_badges_courses
from .serializers import UsersSerializer, UserCoursesSerializer, CoursesSerializer, BadgesSerializer, UserBadgesCoursesSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the intreped index.")


class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersCoursesView(viewsets.ModelViewSet):
    queryset = User_courses.objects.all()
    serializer_class = UserCoursesSerializer


class CoursesView(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class BadgesView(viewsets.ModelViewSet):
    queryset = Badges.objects.all()
    serializer_class = BadgesSerializer

class UserBadgesCoursesView(viewsets.ModelViewSet):
    queryset = User_badges_courses.objects.all()
    serializer_class = UserBadgesCoursesSerializer
