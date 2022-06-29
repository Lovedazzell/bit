from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name
    