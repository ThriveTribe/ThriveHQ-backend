from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Thrive(models.Model):
    # name = models.CharField(max_length=256)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    task = models.TextField(default="", null=True, blank=True)
    is_checked = models.BooleanField(default=0, blank=False)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('thrive_detail', args=[str(self.id)])

