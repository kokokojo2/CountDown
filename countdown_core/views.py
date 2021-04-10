from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView

from .models import Countdown
from .forms import CountdownForm
from .services.countdown_management import create_countdown
from custom_user.views import LoginRequiredView


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


class DashBoardView(ListView, LoginRequiredView):
    model = Countdown
    template_name = 'countdown/dashboard.html'

    def get_queryset(self):
        queryset = super(DashBoardView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class CountdownDeleteView(LoginRequiredView):

    def get(self, request, pk):
        c = Countdown.objects.get(pk=pk)
        return render(request, 'countdown/countdown_delete.html', {'can_delete': request.user == c.user})

    def post(self, request, pk):
        c = Countdown.objects.get(pk=pk)

        if c.user == request.user:
            c.delete()
            return redirect('countdown_core:dashboard')

        return render(request, 'countdown/countdown_delete.html', {'can_delete': request.user == c.user})


class CountdownUpdate(UpdateView, LoginRequiredView):
    model = Countdown
    template_name = 'countdown/countdown_edit.html'
    form_class = CountdownForm
    success_url = reverse_lazy('countdown:dashboard')
