from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse, HttpResponseForbidden

from .models import Countdown, ReactionSet
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

        # TODO: move to a service (use it in js view as well)
        if self.request.user.is_authenticated:
            try:
                reaction_set_obj = ReactionSet.objects.get(user=self.request.user, countdown=self.object)
            except ReactionSet.DoesNotExist:
                reaction_set_obj = None

            context['reaction_set'] = reaction_set_obj

        likes_number = self.object.reactionset_set.filter(like=True).count()
        dislikes_number = self.object.reactionset_set.filter(dislike=True).count()
        laugh_number = self.object.reactionset_set.filter(laugh=True).count()
        cry_number = self.object.reactionset_set.filter(cry=True).count()

        context['likes_number'] = likes_number
        context['dislikes_number'] = dislikes_number
        context['laugh_number'] = laugh_number
        context['cry_number'] = cry_number

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

    reaction_id_dict = {'cry': 0, 'laugh': 1, 'like': 2, 'dislike': 3}

    def get(self, request, pk, reaction_id):

        if request.user.is_authenticated:
            countdown = get_object_or_404(Countdown, pk=pk)
            reaction_set_obj, created = ReactionSet.objects.get_or_create(user=request.user, countdown=countdown)

            if reaction_id == self.reaction_id_dict['cry']:
                reaction_set_obj.cry = not reaction_set_obj.cry
                if reaction_set_obj.cry:
                    reaction_set_obj.laugh = False

            if reaction_id == self.reaction_id_dict['laugh']:
                reaction_set_obj.laugh = not reaction_set_obj.laugh
                if reaction_set_obj.laugh:
                    reaction_set_obj.cry = False

            if reaction_id == self.reaction_id_dict['like']:
                reaction_set_obj.like = not reaction_set_obj.like
                if reaction_set_obj.like:
                    reaction_set_obj.dislike = False

            if reaction_id == self.reaction_id_dict['dislike']:
                reaction_set_obj.dislike = not reaction_set_obj.dislike
                if reaction_set_obj.dislike:
                    reaction_set_obj.like = False

            reaction_set_obj.save()

            likes_number = countdown.reactionset_set.filter(like=True).count()
            dislikes_number = countdown.reactionset_set.filter(dislike=True).count()
            laugh_number = countdown.reactionset_set.filter(laugh=True).count()
            cry_number = countdown.reactionset_set.filter(cry=True).count()

            buttons_state = f', "like_state": {"true" if reaction_set_obj.like else "false"}, "dislike_state": {"true" if reaction_set_obj.dislike else "false"}, "laugh_state": {"true" if reaction_set_obj.laugh else "false"}, "cry_state": {"true" if reaction_set_obj.cry else "false"}}}'
            reaction_numbers = f'{{ "laugh": {laugh_number}, "cry": {cry_number}, "like": {likes_number}, "negative": {dislikes_number}'
            return HttpResponse(reaction_numbers + buttons_state)
        else:
            return HttpResponseForbidden()


class BookmarksServiceView(View):

    def get(self, request, pk):

        if request.user.is_authenticated:
            countdown = Countdown.objects.get(pk=pk)
            qs = request.user.bookmarked_countdowns.filter(pk=pk)

            if len(qs) > 0:
                request.user.bookmarked_countdowns.remove(countdown)
                return HttpResponse('removed')
            else:
                request.user.bookmarked_countdowns.add(countdown)
                return HttpResponse('added')

