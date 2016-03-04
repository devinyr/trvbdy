from django.contrib.auth import login, authenticate, forms, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from apps.dshbrd.models import Destination, TravelPlan


class Dashboard(View):
    def get(self, request):
        dictionary = {
            "tripschdl": TravelPlan.objects.filter(user_id=request.user),
            "otherlist": TravelPlan.objects.exclude(user_id=request.user)
        }
       
        return render(request, "dshbrd/dashboard.html", dictionary)


class Trip(View):
    def get(self,request,id):
        context = {
            "destination": Destination.objects.get(id=id),
            "people": TravelPlan.objects.filter(destination_id=id)
        }
        return render(request, "dshbrd/destination.html", context)


