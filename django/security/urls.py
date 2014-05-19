from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
url(r'^sign-in/', 'security.views.obtain_auth_token_login')
)