from django.db import models
from django.conf import settings
from django.urls import reverse


class Countdown(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    finished = models.DateTimeField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    # TODO: Add a relation to a simple reactions

    def __str__(self):
        return f'Countdown {self.name} created by {self.user}' if self.user else f'Anonymous Countdown {self.name}'

    def url(self):
        return reverse('countdown_core:detail', args=[self.pk])
