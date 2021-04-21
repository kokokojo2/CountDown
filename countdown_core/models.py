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

    like_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='love_reactions')
    cry_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cry_reactions')
    negative_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='negative_reaction')
    laugh_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='lough_reaction')

    def __str__(self):
        return f'Countdown {self.name} created by {self.user}' if self.user else f'Anonymous Countdown {self.name}'

    def get_absolute_url(self):
        return reverse('countdown_core:detail', args=[self.pk])
