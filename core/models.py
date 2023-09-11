from django.db import models

# Create your models here.
class Parent(models.Model):
    name        = models.CharField(max_length=255     , null=True, blank=True)
    age         = models.CharField(max_length=255     , null=True, blank=True)
    gender      = models.CharField(max_length=255     , null=True, blank=True)
    the_job     = models.CharField(max_length=255, null=True, blank=True)
    work_where  = models.CharField(max_length=255, null=True, blank=True)
    livewhere   = models.CharField(max_length=255, null=True, blank=True)
    state_of_mariege = models.CharField(max_length=255, null=True, blank=True)
    
    
    # ifmarried
    married_to = models.ForeignKey(to="self", on_delete=models.SET_NULL, null=True , blank= True )
    # ifx



class Account(models.Model):
    name    =models.CharField(max_length=255)
    gender  =models.CharField(max_length=255, blank=True, null=True)
    age     =models.CharField(max_length=255, blank=True, null=True)
    mother  = models.ForeignKey("Parent",related_name="core.Account.father+", blank=True, null=True, on_delete=models.SET_NULL)
    father  = models.ForeignKey("Parent",related_name="core.Account.mother+", blank=True, null=True, on_delete=models.SET_NULL)
    state_of_marrieg = models.CharField(max_length=255, blank=True, null=True)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    