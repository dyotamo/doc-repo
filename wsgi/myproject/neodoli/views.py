from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.

class Home(View):

	def get(self, request):
		return redirect('/admin')