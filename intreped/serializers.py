from rest_framework import serializers
from models.models import Users, Courses, User_courses, Badges, User_badges_courses

class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = ('id', 'name', 'username', 'password', 'email')


class CoursesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Courses
    fields = ('id', 'title', 'description', 'url', 'category')


class UserCoursesSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_courses
    fields = ('id', 'user_id', 'course_id', 'current_playtime', 'is_favorite', 'is_complete', 'is_in_progress')


class BadgesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Badges
    fields = ('id', 'category')


class UserBadgesCoursesSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_badges_courses
    fields = ('id', 'name', 'user_id', 'badge_id', 'course_id')
