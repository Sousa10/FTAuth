from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ListHeaderT(models.Model):
    PersonFK = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    LHName = models.CharField(max_length=240)
    LHDescription = models.CharField(max_length=240)

    def __str__(self):
        return self.LHName

class ListDetailsT(models.Model):
    ListHeaderFK = models.ForeignKey('ListHeaderT', on_delete=models.CASCADE)
    ListDetailFK = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='predecessor')
    LNNumber = models.IntegerField()
    LHName = models.CharField(max_length=240)

    def __str__(self):
        return self.LHName