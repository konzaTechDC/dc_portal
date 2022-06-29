from tabnanny import verbose
from django.db import models
from django.utils.safestring import mark_safe
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError

BANDWITH = [('Unlimited Bandwidth','Unlimited Bandwidth'),('Unlimited Bandwidth','Unlimited Bandwidth'),('Unlimited Bandwidth','Unlimited Bandwidth'),
    ('300GB Bandwidth','300GB Bandwidth'),('400GB Bandwidth','400GB Bandwidth'),('500GB Bandwidth','500GB Bandwidth'),
    ('600GB Bandwidth','600GB Bandwidth'),('700GB Bandwidth','700GB Bandwidth'),('30TB Bandwidth','30TB Bandwidth')
    ]

SERVICES =[('Cloud Services','Cloud Services'),('Webhosting Services','Webhosting Services'),('Collocation','Collocation')]

COST_PERIOD =[('Month','Month'),('Year','Year')]

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
    name = models.CharField(max_length=30,choices=SERVICES,default=SERVICES[0],unique=True)# e.g Webhosting
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)

    def image_path(self):
        if self.image:
            return mark_safe('<a href="%s"><img src="%s" style="width: 45px; height:45px;" /></a>' % (self.image.url,self.image.url))
    def image_path_only(self):
        if self.image:
            return str(self.image.url)

    
    def __str__(self):
        return str(self.name)


class Category(Common):
    service_name = models.ForeignKey(Service,on_delete=models.CASCADE)
    service_category  = models.CharField(max_length=50) #e.g vdi/Konza Basic Package
    image_file = models.ImageField(upload_to='images')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural ='Categories'
    
    def image_path_only(self):
        if self.image_file:
            return str(self.image_file.url)

    
    def __str__(self):
        return str(self.service_category)

class ServiceType(Common):
    service_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    service_type  = models.CharField(max_length=50) #e.g small/Konza Business Enterprise
    payment_period = models.CharField(max_length=10,choices=COST_PERIOD,default=COST_PERIOD[0])
    cost = models.FloatField(verbose_name='Cost (USD)')
    cpu_type = models.CharField(max_length=6,choices=[('CPU','CPU'),('VCPU','VCPU')],default='VCPU')
    cpu  = models.CharField(max_length=10)
    memory_unit = models.CharField(max_length=4,choices=[('MB','MB'),('GB','GB')],default='GB')
    memory  = models.FloatField()
    disk_type = models.CharField(max_length=15,choices=[('SYSTEM DISK','SYSTEM DISK'),('SAS','SAS')],default='SYSTEM DISK')
    disk  = models.CharField(max_length=15,verbose_name='DISK (GB)')
    bandwidth = models.CharField(max_length=50,choices=BANDWITH,default=BANDWITH[0])

    def __str__(self):
        return str(self.service_name)