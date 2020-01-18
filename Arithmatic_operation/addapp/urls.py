from django.conf.urls import url
from . import views
app_name='addapp'
urlpatterns=[
    url(r'^$', views.input),
    url(r'^add$', views.add),
    url(r'^sub$', views.sub),
    url(r'^mul$', views.mul),
    url(r'^div$', views.div),
    url(r'^floor$', views.floor),
]