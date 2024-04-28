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
    receivers = ArrayField(ArrayField(models.CharField(max_length=255)), blank=True)

    def __str__(self):
        return f"{self.name} - {self.owner}"


class NotificationTemplate(models.Model):
    name = models.CharField(max_length=40)
    text = models.TextField(max_length=120)
    group = models.ForeignKey(
        to='templates.UserGroup',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='group_templates'
    )

    def __str__(self):
        return f"{self.name} - {self.group.name}"
