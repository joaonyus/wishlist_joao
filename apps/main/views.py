# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *
from ..log_reg.models import *
from django.contrib import messages

# Create your views here.

def index(req):
    
    context = {
        'user_in_session': req.session['first_name'],
        'user_id_in_session': req.session['user_id'],
        'my_travels':Travel.objects.filter(created_by=req.session['user_id']),
        'joined_travels':Travel.objects.filter(joined_by=req.session['user_id']),
        'all_travels': Travel.objects.exclude(joined_by=req.session['user_id']).order_by('-created_at'),
    }
    return render(req,'main/index.html', context)

def travel_form(req):
    context = {
        'user_id': req.session['user_id'],
        'user_in_session': req.session['first_name'],
    }
    return render(req, 'main/traveladd.html', context)

def travel_post(req,user_id):
    errors = Travel.objects.validate_travel(req.POST)

    if errors:
        for tag,error in errors.iteritems():
            messages.error(req,error,extra_tags=tag)
        return redirect('/travel/add')

    travel_plan = Travel.objects.create_travel(req.POST, user_id)

    return redirect('/travel')

def travel_show(req,travel_id):
    travel = Travel.objects.get(id=travel_id)
    users_joined = users.objects.filter(joined=travel_id)
    
    print users_joined

    context = {
        'travel':travel,
        'users_joined':users_joined,
        'user_id': req.session['user_id'],
        'user_in_session': req.session['first_name']
    }
    return render(req,'main/travel.html', context)

def user_show(req, user_id):
    user = users.objects.get(id=user_id)
    context = {
        'user': user.email_address,
        'user_in_session': req.session['first_name'],
        'first_name': user.first_name,
        'last_name': user.last_name,
        'reviews': user.reviews_left.count(),
        'books': user.reviews_left.all()

    }
    return render(req, 'main/userinfo.html', context)

def delete_travel(req, travel_id):
    travel_delete = Travel.objects.get(id=travel_id)
    travel_delete.delete()
    
    return redirect('/travel')

def join_travel(req, travel_id, user_id):
    travel_joining = Travel.objects.get(id=travel_id)
    user_joining = users.objects.get(id=user_id) 

    travel_joining.joined_by.add(user_joining)
    
    return redirect('/travel')

def unjoin_travel(req, travel_id, user_id):
    travel_unjoining = Travel.objects.get(id=travel_id)
    user_unjoining = users.objects.get(id=user_id) 

    travel_unjoining.joined_by.remove(user_unjoining)
    
    return redirect('/travel')