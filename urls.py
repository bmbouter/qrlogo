from django.conf.urls.defaults import patterns, include, url
from django.conf import settings   
import views
import settings

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home_url'),
    url(r'^make/$', views.MakeView.as_view(), name='make_url'),
    url(r'^images/$', views.ImagesView.as_view(), name='images_url'),
    url(r'^images/delete/$', views.DeleteImage, name='delete_image_url'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login_url'),
    url(r'^accounts/passreset/$', views.PassReset, name='pass_reset_url'),
    url(r'^accounts/logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout_url'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', views.ServeImage, name='serve_image_url'),
    )