from tabnanny import verbose
from django.db import models
from django.utils.safestring import mark_safe
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
class Servic(models.Model):
    service_name = models.CharField(max_length=150,verbose_name='service name')#e.g Webhosting
    image = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.TextField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<a href="%s"><img src="%s" style="width: 45px; height:45px;" /></a>' % (self.image.url,self.image.url))


    def __str__(self):
        return mark_safe() 

class CloudService(models.Model):
    cloud_service_name = models.CharField(max_length=150,verbose_name='service name')#e.g virtual machine
    image = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.TextField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<a href="%s"><img src="%s" style="width: 45px; height:45px;" /></a>' % (self.image.url,self.image.url))


    def __str__(self):
        return str(self.cloud_service_name)

class CloudServiceFlavour(models.Model):
    cloud_service_name = models.ForeignKey(CloudService,on_delete=models.CASCADE)
    service_type  = models.CharField(max_length=50)
    cost = models.FloatField(verbose_name='Cost USD/Month')
    image = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.TextField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<a href="%s"><img src="%s" style="width: 45px; height:45px;" /></a>' % (self.image.url,self.image.url))

    def __str__(self):
        return str(self.cloud_service_name)

class CloudServiceHardwareResource(models.Model):
    cloud_service_name = models.ForeignKey(CloudServiceFlavour,on_delete=models.CASCADE)
    cpu_type = models.CharField(max_length=6,choices=[('CPU','CPU'),('VCPU','VCPU')],default='VCPU')
    cpu  = models.IntegerField()
    memory  = models.FloatField(verbose_name='Memory (GB)')
    disk_type = models.CharField(max_length=15,choices=[('SYSTEM DISK','SYSTEM DISK'),('SAS','SAS')],default='SYSTEM DISK')
    disk  = models.FloatField(verbose_name='DISK (GB)')

    def __str__(self):
        return str(self.cloud_service_name)

class CloudServiceOtherFeature(models.Model):
    cloud_service_name = models.ForeignKey(CloudServiceFlavour,on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)

    def __str__(self):
        return str(self.cloud_service_name)

class Webhosting(models.Model):
    webhosting_service_name = models.CharField(max_length=150,verbose_name='service name')#e.g konza basic package
    image = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.TextField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<a href="%s"><img src="%s" style="width: 45px; height:45px;" /></a>' % (self.image.url,self.image.url))

    def __str__(self):
        return str(self.webhosting_service_name)

class WebhostingFlavour(models.Model):
    webhosting_service_name = models.ForeignKey(Webhosting,on_delete=models.CASCADE)
    service_type  = models.CharField(max_length=50)
    cost_period = models.CharField(max_length=6,choices=[('Year','Year'),('Month','Month')],default='USD/Month')
    cost = models.FloatField(verbose_name='Cost (USD)')
    image = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.TextField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<a href="%s"><img src="%s" style="width: 45px; height:45px;" /></a>' % (self.image.url,self.image.url))


    def __str__(self):
        return str(self.webhosting_service_name)
BANDWITH = [('Unlimited Bandwidth','Unlimited Bandwidth'),('Unlimited Bandwidth','Unlimited Bandwidth'),('Unlimited Bandwidth','Unlimited Bandwidth'),
    ('300GB Bandwidth','300GB Bandwidth'),('400GB Bandwidth','400GB Bandwidth'),('500GB Bandwidth','500GB Bandwidth'),
    ('600GB Bandwidth','600GB Bandwidth'),('700GB Bandwidth','700GB Bandwidth'),('30TB Bandwidth','30TB Bandwidth')
    ]
class WebhostingHardwareREsource(models.Model):
    
    webhosting_service_name = models.ForeignKey(WebhostingFlavour,on_delete=models.CASCADE)
    cpu_type = models.CharField(max_length=6,choices=[('CPU','CPU'),('VCPU','VCPU')],default='VCPU')
    cpu  = models.IntegerField()
    memory_unit = models.CharField(max_length=4,choices=[('MB','MB'),('GB','GB')],default='GB')
    memory  = models.FloatField()
    disk  = models.FloatField(verbose_name='SYSTEM DISK (GB)')
    bandwidth = models.CharField(max_length=50,choices=BANDWITH,default=BANDWITH[0])

    def __str__(self):
        return str(self.webhosting_service_name)

class WebhostingOtherFeature(models.Model):
    webhosting_service_name = models.ForeignKey(WebhostingFlavour,on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)

    def __str__(self):
        return str(self.webhosting_service_name)



class TopLevel(models.Model):
    name = models.CharField(max_length=200)

class LevelOne(models.Model):
    name = models.CharField(max_length=200)
    level = models.ForeignKey('TopLevel',on_delete=models.CASCADE)

class LevelTwo(models.Model):
    name = models.CharField(max_length=200)
    level = models.ForeignKey('LevelOne',on_delete=models.CASCADE)

class LevelThree(models.Model):
    name = models.CharField(max_length=200)
    level = models.ForeignKey('LevelTwo',on_delete=models.CASCADE)


SERVICES =[(1,'Cloud Services'),(2,'Webhosting Services'),(3,'Collocation')]
COST_PERIOD =[(0,'Month'),(1,'Year')]

def Validate_disk_space(space):
    splinted = str(space).split('*')
    if str(space).isdecimal() == True:
        return space
    elif len(splinted)==2 and str(splinted[0]).isdecimal()==True and str(splinted[1]).isdecimal() ==True:
        return space
    else:
        raise ValidationError('Space should be integer or  2*300 format')

class Common(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    history  =HistoricalRecords(inherit=True)

    
    
    class Meta:
        abstract = True

class Service(models.Model):
    name = models.IntegerField(choices=SERVICES,default=SERVICES[0],unique=True)# e.g Webhosting
    image = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.CharField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<a href="%s"><img src="%s" style="width: 45px; height:45px;" /></a>' % (self.image.url,self.image.url))

    
    def __str__(self):
        for i in SERVICES:
            if str(i[0])==str(self.name):
                return str(i[1])


class Category(Common):
    service_name = models.ForeignKey(Service,on_delete=models.CASCADE)
    service_category  = models.CharField(max_length=50) #e.g vdi/Konza Basic Package
    image = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.CharField(max_length=200,blank=True,null=True)

    class Meta:
        verbose_name_plural ='Categories'

    def image_path(self):
        if self.image:
            return mark_safe('<a href="%s"><img src="%s" style="width: 45px; height:45px;" /></a>' % (self.image.url,self.image.url))


    def __str__(self):
        return str(self.service_name)

class ServiceType(Common):
    service_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    service_type  = models.CharField(max_length=50) #e.g small/Konza Business Enterprise
    payment_period = models.IntegerField(choices=COST_PERIOD,default=COST_PERIOD[0])
    cost = models.FloatField(verbose_name='Cost (USD)')
    cpu_type = models.CharField(max_length=6,choices=[('CPU','CPU'),('VCPU','VCPU')],default='VCPU')
    cpu  = models.CharField(max_length=10)
    memory_unit = models.CharField(max_length=4,choices=[('MB','MB'),('GB','GB')],default='GB')
    memory  = models.FloatField()
    disk_type = models.CharField(max_length=15,choices=[('SYSTEM DISK','SYSTEM DISK'),('SAS','SAS')],default='SYSTEM DISK')
    disk  = models.CharField(max_length=15,verbose_name='DISK (GB)')
    bandwidth = models.CharField(max_length=50,choices=BANDWITH,default=BANDWITH[0])

    def image_path(self):
        if self.image:
            return mark_safe('<a href="%s"><img src="%s" style="width: 45px; height:45px;" /></a>' % (self.image.url,self.image.url))


    def __str__(self):
        return str(self.service_name)


