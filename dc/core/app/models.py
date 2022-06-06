from django.db import models
from django.utils.translation import ugettext_lazy as _
# contact us

class ContactUs(models.Model):
    name = models.CharField(
        _('name'),
        max_length=40,
        error_messages={
            'name': 'Name too long.'
        }
    )
    email = models.EmailField(
        _('email'),
        unique=True,
        error_messages={
            'email': 'Email taken. Use a different one.'
        }
    )
    phone = models.CharField(
        _('phone number'),
        max_length=10,
        unique=True, 
        error_messages={
            "phone": "Phone number too long."
        }
    )
    message = models.TextField(
        _('message'),
        max_length= 1000,
        null=False,
        blank=False,
        error_messages= {
            "max_lenght": "The message exceeds allowed character limit."
        }

    )

    def __str__(self):
        return self.name 




