# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..log_reg.models import *
from django.db import models

# Create your models here.

class DataManager(models.Manager):
    def validate_travel(self, postData):
        errors = {}

        if len(postData['destination'])<3:
            errors['data']='Entry must have more than 3 characters'

        if len(postData['destination'])<1:
            errors['data']='No empty entries are allowed'
            
        return errors

    def create_travel(self,postData,user_id):
        
        traveler = users.objects.get(id=user_id)
        this_travel = postData['destination']

        Travel.objects.create(destination=postData['destination'], created_by=traveler)

        return this_travel

####

class Travel(models.Model):
    destination = models.CharField(max_length=100)
    created_by = models.ForeignKey(users, related_name='creator')
    joined_by = models.ManyToManyField(users,related_name='joined')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DataManager()

    def __str__(self):
        return self.destination