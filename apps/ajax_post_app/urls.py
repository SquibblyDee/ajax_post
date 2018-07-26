from django.conf.urls import url
from . import views

urlpatterns = [
    # root goes to the index
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^all.json$', views.all_json),
    url(r'^all.html$', views.all_html),

]