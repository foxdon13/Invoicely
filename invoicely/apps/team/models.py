from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    org_number = models.CharField(max_length=255,blank=True,null=True)
    first_invoice_number = models.IntegerField(default=1)
    created_by = models.ForeignKey(User,related_name='teams',on_delete=models.CASCADE)

    def str(self):
        return f"{self.name}"