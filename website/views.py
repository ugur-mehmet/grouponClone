from django.shortcuts import render, render_to_response
from admin.models import Campaign
# Create your views here.

def home(request):
	campaign_list = Campaign.objects.all()
	return render_to_response("website/home.html",{'campaign_list':campaign_list})