from django.db import models
from django.contrib.postgres.fields import ArrayField


class UserGroup(models.Model):
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(
        to='authentication.CustomUser',
        related_name='user_groups',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    receivers = ArrayField(ArrayField(models.CharField(max_length=255)))


class Template(models.Model):
    name = models.CharField(max_length=40)
    text = models.TextField(max_length=120)
    group = models.OneToOneField('templates.UserGroup', on_delete=models.PROTECT, related_name='templates')
