from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
from models import *
from forms import *
from website.models import TestModel

# Create your views here.
def login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'],
							password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('/admin/index')
	c = {}
	c.update(csrf(request))
	return render_to_response('admin/login.html',c)

@login_required(login_url='/admin/login')
def index(request):
	campaign_list = Campaign.objects.all()
	return render_to_response('admin/index.html',{'campaign_list':campaign_list})

@login_required(login_url='/admin/login')
def new_campaign(request):
	if request.method == 'POST':
		form = CampaignForm(request.POST)
		if form.is_valid():
			#Campaign is saved here
			campaign = Campaign(name=form.cleaned_data.get('name'),
								content=form.cleaned_data.get('content'),
								price=form.cleaned_data.get('price'),
								start_date=form.cleaned_data.get('start_date'),
								end_date=form.cleaned_data.get('end_date'))
			campaign.save()
			return redirect('/admin/index')
	else:
		form = CampaignForm()
	c = {"form": form}
	c.update(csrf(request))
	return render_to_response('admin/new_campaign.html',c)

@login_required(login_url='/admin/login')
def edit_campaign(request,campaign_id):
	campaign = Campaign.objects.get(id=campaign_id)
	if request.method == 'POST':
		form = CampaignForm(request.POST)
		if form.is_valid():
			#Campaign is saved here
			campaign.name = form.cleaned_data.get('name')
			campaign.content = form.cleaned_data.get('content')
			campaign.price = form.cleaned_data.get('price')
			campaign.start_date = form.cleaned_data.get('start_date')
			campaign.end_date = form.cleaned_data.get('end_date')
			campaign.save()
			return redirect('/admin/index')
	else:
		form = CampaignForm(initial={'name':campaign.name, "content":campaign.content,
									'price':campaign.price, "start_date":campaign.start_date,
									'end_date': campaign.end_date})
	c = {"form": form, "campaign_id": campaign.id}
	c.update(csrf(request))
	return render_to_response('admin/edit_campaign.html',c)

@login_required(login_url='/admin/login')
def delete_campaign(request,campaign_id):
	campaign = Campaign.objects.get(id=campaign_id)
	campaign.delete()
	return redirect('/admin/index')

@login_required(login_url='/admin/login')
def logout(request):
	auth.logout(request)
	return redirect('/admin/login')

def home(request,word):
	campaign_list = Campaign.objects.all()
	return render_to_response("website/home.html",{'campaign_list':campaign_list, 'word': word})

