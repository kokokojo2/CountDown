from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse, HttpResponseForbidden

from .models import Countdown
from custom_user.models import CustomUser
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            self.object.like_reaction.get(pk=self.request.user.pk)
            context['like_enabled'] = True
        except CustomUser.DoesNotExist:
            context['like_enabled'] = False

        try:
            self.object.negative_reaction.get(pk=self.request.user.pk)
            context['dislike_enabled'] = True
        except CustomUser.DoesNotExist:
            context['dislike_enabled'] = False

        try:
            self.object.laugh_reaction.get(pk=self.request.user.pk)
            context['laugh_enabled'] = True
        except CustomUser.DoesNotExist:
            context['laugh_enabled'] = False

        try:
            self.object.cry_reaction.get(pk=self.request.user.pk)
            context['cry_enabled'] = True
        except CustomUser.DoesNotExist:
            context['cry_enabled'] = False

        return context


class DashBoardView(ListView, LoginRequiredView):
    model = Countdown
    template_name = 'countdown/dashboard.html'

    def get_queryset(self):
        queryset = super(DashBoardView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class CountdownUpdateView(UpdateView, LoginRequiredView, UserPassesTestMixin):
    model = Countdown
    template_name = 'countdown/countdown_edit.html'
    form_class = CountdownForm

    def test_func(self):
        return Countdown.objects.get(pk=self.kwargs['pk']).user == self.request.user


class CountdownDeleteView(DeleteView, LoginRequiredView, UserPassesTestMixin):
    model = Countdown
    template_name = 'countdown/countdown_delete.html'
    success_url = reverse_lazy('countdown:dashboard')

    def test_func(self):
        return Countdown.objects.get(pk=self.kwargs['pk']).user == self.request.user


class CountdownFinishedServiceView(View):
    """
    This view is used by js function to asynchronously get finished text.
    """
    def get(self, request, pk):
        countdown_obj = get_object_or_404(Countdown, pk=pk)
        timedelta_seconds = int((countdown_obj.finished.replace(tzinfo=None) - datetime.now()).total_seconds())

        if timedelta_seconds <= 0:
            return HttpResponse(countdown_obj.finished_text)

        return HttpResponseForbidden()


class ReactionServiceView(View):

    reaction_id_dict = {'cry': 0, 'laugh': 1, 'like': 2, 'negative': 3}

    def get(self, request, pk, reaction_id):

        if request.user.is_authenticated:
            countdown = get_object_or_404(Countdown, pk=pk)

            if reaction_id == self.reaction_id_dict['cry']:
                user_queryset = countdown.cry_reaction.filter(pk=request.user.pk)

                if len(user_queryset) > 0:
                    countdown.cry_reaction.remove(request.user)

                else:
                    countdown.cry_reaction.add(request.user)

            if reaction_id == self.reaction_id_dict['laugh']:
                user_queryset = countdown.laugh_reaction.filter(pk=request.user.pk)

                if len(user_queryset) > 0:
                    countdown.laugh_reaction.remove(request.user)

                else:
                    countdown.laugh_reaction.add(request.user)

            if reaction_id == self.reaction_id_dict['like']:
                user_queryset = countdown.like_reaction.filter(pk=request.user.pk)

                if len(user_queryset) > 0:
                    countdown.like_reaction.remove(request.user)

                else:
                    countdown.like_reaction.add(request.user)

            if reaction_id == self.reaction_id_dict['negative']:
                user_queryset = countdown.negative_reaction.filter(pk=request.user.pk)

                if len(user_queryset) > 0:
                    countdown.negative_reaction.remove(request.user)

                else:
                    countdown.negative_reaction.add(request.user)
