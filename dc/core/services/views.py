from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Service,Category,ServiceType

def all_services(request,servicetype):
    context = {}
    service = Service.objects.get(name='Cloud Services')
    category = Category.objects.filter(service_name_id=service.id)
    sub_category = ServiceType.objects.all()
    context['service'],context['category'],context['sub_category']= service,category,sub_category
    context['level'] = 1
    return render(request=request,template_name='categories.html',context=context)

def category(request,index):
    context = {}
    service = Category.objects.get(id=index)
    context['previous'] = Service.objects.get(id=service.service_name_id).name
    category = ServiceType.objects.filter(service_name_id=service.id)
    context['service'],context['category']= service,category
    context['level'] = 2
    return render(request=request,template_name='categories.html',context=context)
    print(index)

def flavours(request):
    context = {}
    service = Service.objects.get(name='Cloud Services')
    category = Category.objects.filter(service_name_id=service.id)
    sub_category = ServiceType.objects.all()
    context['service'],context['category'],context['sub_category']= service,category,sub_category
    context['level'] = 1
    return render(request=request,template_name='categories.html',context=context)

def webhosting(request):
    context = {}
    service = Service.objects.get(name='Webhosting Services')
    category = Category.objects.filter(service_name_id=service.id)
    sub_category = ServiceType.objects.all()
    context['service'],context['category'],context['sub_category']= service,category,sub_category
    return render(request=request,template_name='services_base.html',context=context)


