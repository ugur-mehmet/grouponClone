from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blog/', include('blog.urls')),

	#url(r'^(?P<word>\w+)/', 'admin.views.home', name='home'),

	url(r'^admin/login$', 'admin.views.login', name='admin.login'),
	url(r'^admin/logout$', 'admin.views.logout', name='admin.logout'),
	url(r'^admin/index$', 'admin.views.index', name='admin.index'),
	url(r'^admin/new_campaign$', 'admin.views.new_campaign', name='admin.new_campaign'),
	url(r'^admin/edit_campaign/(?P<campaign_id>\d)/$', 'admin.views.edit_campaign', name='admin.edit_campaign'),
	url(r'^admin/delete_campaign/(?P<campaign_id>\d)/$', 'admin.views.delete_campaign', name='admin.delete_campaign'),
    #url(r'^admin/', include(admin.site.urls)),
)
