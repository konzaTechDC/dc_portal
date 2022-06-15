from django.contrib import admin
from .models import CloudService,CloudServiceFlavour,CloudServiceHardwareResource,CloudServiceOtherFeature
from .models import Webhosting,WebhostingFlavour,WebhostingHardwareREsource,WebhostingOtherFeature,Service

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

class WebhostingHardwareREsourceInline(admin.TabularInline):
    model = WebhostingHardwareREsource
    min_num=1
    max_num=1

class WebhostingOtherFeatureInline(admin.TabularInline):
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

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name','image_path','description']
    search_fields= ['service_name',]

#admin.site.register(Service,ServiceAdmin)



from nested_inline.admin import NestedStackedInline, NestedModelAdmin,NestedTabularInline
from .models import *

class LevelThreeInline(NestedTabularInline):
    model = LevelThree
    extra = 1
    fk_name = 'level'


class LevelTwoInline(NestedStackedInline):
    model = LevelTwo
    extra = 1
    fk_name = 'level'
    inlines = [LevelThreeInline]


class LevelOneInline(NestedStackedInline):
    model = LevelOne
    extra = 1
    fk_name = 'level'
    inlines = [LevelTwoInline]


class TopLevelAdmin(NestedModelAdmin):
    model = TopLevel
    inlines = [LevelOneInline]


admin.site.register(TopLevel, TopLevelAdmin)



class ServiceTypeInline(NestedTabularInline):
    model = ServiceType
    extra = 0
    fk_name = 'service_name'



class CategoryInline(NestedTabularInline):
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
