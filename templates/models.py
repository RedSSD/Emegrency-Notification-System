from django.db import models
from django.contrib.postgres.fields import ArrayField


class UserGroup(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    owner = models.ForeignKey(
        to='authentication.CustomUser',
        related_name='user_groups',
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    receivers = ArrayField(ArrayField(models.CharField(max_length=255)), blank=True)

    def __str__(self):
        return f"{self.name} - {self.owner}"


class NotificationTemplate(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    text = models.TextField(max_length=120, blank=False, null=False)
    group = models.ForeignKey(
        to='templates.UserGroup',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='group_templates'
    )

    def __str__(self):
        return f"{self.name} - {self.group.name}"
