from django.contrib import admin
from django.urls import path


from loanservices import views
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from rest_framework import routers
from django.http import HttpResponseRedirect

schema_view = get_swagger_view(title='API name')
'''
router = routers.DefaultRouter()
router.register(r'Insurances',createInsurance.)
'''



urlpatterns = [

    url(r'^docs/$', schema_view, name="schema_view"), #swagger -- rest api
   # path('post/', CreateLoan.as_view()),
    #path('get/', GetLoan.as_view()),
    url(r'^loan/$', views.loan_list),
    url(r'^loan/(?P<pk>[0-9]+)$',views.loan_detail),
    url(r'^tranct/$', views.tranct_list),


]



#pip install django-rest-swagger