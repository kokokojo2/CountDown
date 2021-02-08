from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from .models import Countdown
from .forms import CountdownForm
from .services.countdown_management import create_countdown


class CountdownCreateView(View):
    template_name = 'countdown/countdown_create.html'

    def get(self, request):
        return render(request, self.template_name, {'form': CountdownForm()})

    def post(self, request):
        countdown_form = CountdownForm(request.POST)
        countdown = create_countdown(countdown_form, request.user)

        if countdown:
            return redirect(countdown)

        return render(request, self.template_name, {'form': countdown_form})


class CountdownDetailView(DetailView):
    model = Countdown
    context_object_name = 'countdown'
    template_name = 'countdown/countdown_detail.html'
