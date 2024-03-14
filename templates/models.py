from django.db import models
from django.contrib.postgres.fields import ArrayField


class UserGroup(models.Model):
    name = models.CharField(max_length=40)
    templates = models.ForeignKey('templates.Template', on_delete=models.CASCADE, related_name='user_group')
    receivers = ArrayField(ArrayField(models.CharField(max_length=255)))


class Template(models.Model):
    name = models.CharField(max_length=40)
    text = models.TextField(max_length=120)

