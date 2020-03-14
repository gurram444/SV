from django.contrib import admin
from django.urls import path
from visitor.views import Index,CreateVisit,EmployeeVisit
from visitor import views
urlpatterns = [
    path('index', Index.as_view()),
    path('visit', CreateVisit.as_view()),
    path('evisit',EmployeeVisit.as_view()),
    path('checkin/<int:visitor_id>/',views.check,name='check'),
    ]