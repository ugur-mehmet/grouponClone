from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Campaign(models.Model):
	name = models.CharField(max_length=200)
	content = models.TextField()
	price = models.FloatField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	category = models.ForeignKey(Category,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class CampaignOrders(models.Model):
	ordered_by = models.ForeignKey(User)
	campaign = models.ForeignKey(Campaign)
	ticket_no = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)