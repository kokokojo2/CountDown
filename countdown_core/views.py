from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Countdown
from .forms import CountdownForm


class CountdownCreateView(View):
    template_name = 'countdown/countdown_create.html'

    def get(self, request):
        countdown_form = CountdownForm()
        return render(request, self.template_name, {'form': countdown_form})

    def post(self, request):
        countdown_form = CountdownForm(request.POST)

        # TODO: implement user stuff when the user is done
        if countdown_form.is_valid():
            new_countdown = countdown_form.save()

            # TODO: redirect to detail url if ready
            return HttpResponse('The countdown was created.')

        return render(request, self.template_name, {'form': countdown_form})


class CountdownDetailView(DetailView):
    model = Countdown
    context_object_name = 'countdown'
    template_name = 'countdown/countdown_detail.html'
