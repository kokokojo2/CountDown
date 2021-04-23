from django.db import models
from django.conf import settings
from django.urls import reverse


class Countdown(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    finished = models.DateTimeField()
    finished_text = models.TextField(blank=True, max_length=256)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Countdown {self.name} created by {self.user}' if self.user else f'Anonymous Countdown {self.name}'

    def get_absolute_url(self):
        return reverse('countdown_core:detail', args=[self.pk])


class ReactionSet(models.Model):
    """
    Stores the state of reactions of a particular user on a countdown.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    countdown = models.ForeignKey(Countdown, on_delete=models.CASCADE)

    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    laugh = models.BooleanField(default=False)
    cry = models.BooleanField(default=False)

