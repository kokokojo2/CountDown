from django.shortcuts import render
from django.views import View


class HomePageView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home/homepage_authenticated.html')
        else:
            return render(request, 'home/homepage.html')
