from django.urls import path

from . import views

urlpatterns =[
    path('',views.download_xml_file, name='index')

]