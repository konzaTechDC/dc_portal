from django.contrib import admin
from .models import CloudService,CloudServiceFlavour,CloudServiceHardwareResource,CloudServiceOtherFeature
from .models import Webhosting,WebhostingFlavour,WebhostingHardwareREsource,WebhostingOtherFeature

class CloudServiceHardwareResourceInline(admin.StackedInline):
    model = CloudServiceHardwareResource
    min_num=1
    max_num=1

class CloudServiceOtherFeatureInline(admin.StackedInline):
    model = CloudServiceOtherFeature

class CloudServiceFlavourAdmin(admin.ModelAdmin):
    inlines = [CloudServiceHardwareResourceInline,CloudServiceOtherFeatureInline]
    list_display = ['cloud_service_name','service_type','cost','image_path']
    list_filter= ['cloud_service_name','service_type']
    search_fields= ['cloud_service_name','service_type']


admin.site.register(CloudServiceFlavour,CloudServiceFlavourAdmin)

class CloudServiceAdmin(admin.ModelAdmin):
    list_display = ['cloud_service_name','image_path']
    search_fields= ['cloud_service_name',]

admin.site.register(CloudService,CloudServiceAdmin)

class WebhostingHardwareREsourceInline(admin.StackedInline):
    model = WebhostingHardwareREsource
    min_num=1
    max_num=1

class WebhostingOtherFeatureInline(admin.StackedInline):
    model = WebhostingOtherFeature
    

class WebhostingFlavourAdmin(admin.ModelAdmin):
    inlines = [WebhostingHardwareREsourceInline,WebhostingOtherFeatureInline]
    list_display = ['webhosting_service_name','service_type','cost_period','cost','image_path']
    list_filter= ['webhosting_service_name','service_type','cost_period']
    search_fields= ['webhosting_service_name','service_type','cost_period']

admin.site.register(WebhostingFlavour,WebhostingFlavourAdmin)

class WebhostingAdmin(admin.ModelAdmin):
    list_display = ['webhosting_service_name','image_path']
    search_fields= ['webhosting_service_name',]

admin.site.register(Webhosting,WebhostingAdmin)