from django.db import models


class users(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=60)
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=15)
  email = models.CharField(max_length=25)

class user_courses(models.Model):
  id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(users, on_delete=models.CASCADE)
  course_id = models.ForeignKey(courses, on_delete=models.CASCADE)
  current_playtime = models.CharField(max_length=10)
  is_favorite = models.BooleanField(default=False)
  is_complete = models.BooleanField(default=False)
