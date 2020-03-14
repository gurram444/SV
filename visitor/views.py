from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.


class Index(View):
    template='index.html'

    def get(self,request):
        form=VisitorForm()
        return render(request,self.template,{'form':form})

    def post(self,request):
        form=VisitorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'index1.html',{'form':form})
        return render(request,self.template,{'form':form})


class CreateVisit(View):
    template='visit.html'

    def get(self,request):
        form=VisitForm()
        return render(request,self.template,{'form':form})

    def post(self,request):
        form=VisitForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("saved successfully")
        return render(request,self.template,{'form':form})


class EmployeeVisit(View):
    template='employee.html'

    def get(self, request):
        form = EmployeeForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("saved successfully")
        return render(request, self.template, {'form': form})


def check(request,visitor_id):
    check_in=Visit.objects.get(visitor_id=visitor_id)

    return render(request,'check.html',{'data':check_in})


