
from django.db import models
from django.utils.safestring import mark_safe

class CloudService(models.Model):
    cloud_service_name = models.CharField(max_length=150,verbose_name='service name')#e.g virtual machine
    image = models.ImageField(upload_to='images',null=True,blank=True)
    decription = models.TextField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)

    def __str__(self):
        return str(self.cloud_service_name)

class CloudServiceFlavour(models.Model):
    cloud_service_name = models.ForeignKey(CloudService,on_delete=models.CASCADE)
    service_type  = models.CharField(max_length=50)
    cost = models.FloatField(verbose_name='Cost USD/Month')
    image = models.ImageField(upload_to='images',null=True,blank=True)
    decription = models.TextField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)


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
    decription = models.TextField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)


    def __str__(self):
        return str(self.webhosting_service_name)

class WebhostingFlavour(models.Model):
    webhosting_service_name = models.ForeignKey(Webhosting,on_delete=models.CASCADE)
    service_type  = models.CharField(max_length=50)
    cost_period = models.CharField(max_length=6,choices=[('Year','Year'),('Month','Month')],default='USD/Month')
    cost = models.FloatField(verbose_name='Cost (USD)')
    image = models.ImageField(upload_to='images',null=True,blank=True)
    decription = models.TextField(max_length=200,blank=True,null=True)

    def image_path(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)


    def __str__(self):
        return str(self.webhosting_service_name)

class WebhostingHardwareREsource(models.Model):
    BANDWITH = [('Unlimited Bandwidth','Unlimited Bandwidth'),('Unlimited Bandwidth','Unlimited Bandwidth'),
    ('300GB Bandwidth','300GB Bandwidth'),('400GB Bandwidth','400GB Bandwidth'),('500GB Bandwidth','500GB Bandwidth'),
    ('600GB Bandwidth','600GB Bandwidth'),('700GB Bandwidth','700GB Bandwidth'),('30TB Bandwidth','30TB Bandwidth')
    ]
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
