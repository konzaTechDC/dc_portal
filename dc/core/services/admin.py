from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin,NestedTabularInline
from .models import *



class ServiceTypeInline(NestedTabularInline):
    model = ServiceType
    extra = 0
    fk_name = 'service_name'



class CategoryInline(NestedStackedInline):
    model = Category
    extra = 0
    fk_name = 'service_name'
    inlines = [ServiceTypeInline]


class ServiceAdmin(NestedModelAdmin):
    model = Service
    extra = 0
    inlines = [CategoryInline]
    list_display =['name','image_path','description']


admin.site.register(Service, ServiceAdmin)
