from django import forms

class CampaignForm(forms.Form):
	name = forms.CharField(max_length=200)
	content = forms.CharField(error_messages={'required': 'Bu alan gerekli'})
	price = forms.FloatField()
	start_date = forms.DateTimeField(error_messages={'invalid':'Tarih alani hatali'})
	end_date = forms.DateTimeField(error_messages={'invalid':'Tarih alani hatali'})