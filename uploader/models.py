from django.db import models
from django.utils import timezone

class UserFile(models.Model):
    upload = models.FileField('Upload a File')
    expireDate = models.DateTimeField('expiration time') #add timezone.now() + datetime.timedelta(days=2)
    def __str__(self):
        return self.upload.name
    def expired(self):
        return self.expireDate <= timezone.now()