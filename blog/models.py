from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=255,default='SOME STRING')
    pub_date = models.DateTimeField()
    body = models.TextField(default='SOME STRING')
    image=models.ImageField(upload_to='image')
