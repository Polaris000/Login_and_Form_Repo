from django.views import generic
from .models import Player, Problem, Level
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login     # verifies login
from django.views.generic import View
# from .forms import ChiefLogin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth

def index(request):
   if request.user.is_authenticated():
      return render(request, "L_F_app/index.html")
   else:
      return HttpResponseRedirect("accounts/login/")