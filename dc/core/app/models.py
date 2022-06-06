from django.db import models

# contact us

class ContactUs(models.Model):
    name = models.CharField(verbose_name='Your Name', max_length=50)
    email = models.EmailField(verbose_name='Your Email Address', unique=True)
    phone = models.CharField(verbose_name='Your Phone Number', max_length=10, unique=True)
    message = models.TextField(verbose_name='Your message', max_length=1000)

    def __str__(self):
        return self.name 




