from django.db import models


class Users(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=60)
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=15)
  email = models.CharField(max_length=25)

class Courses(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=20)
  description = models.CharField(max_length=300)
  url = models.CharField(max_length=300)
  category = models.CharField(max_length=15)

class User_courses(models.Model):
  id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
  course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
  current_playtime = models.CharField(max_length=10)
  is_favorite = models.BooleanField(default=False)
  is_complete = models.BooleanField(default=False)
  is_in_progress = models.BooleanField(default=False)


class Badges(models.Model):
  id = models.AutoField(primary_key=True)
  category = models.CharField(max_length=15)

class User_badges_courses(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=10)
  user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
  badge_id = models.ForeignKey(Badges, on_delete=models.CASCADE)
  course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
