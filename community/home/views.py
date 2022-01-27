from os import name, remove
from django.contrib.auth.models import User
from django.forms.forms import Form
from django.forms.formsets import formset_factory
from django.shortcuts import render, redirect
from prawcore.exceptions import InvalidToken
from .forms import CommForm, AddForm, UserRegisterForm, RemoveForm
import praw
from bs4 import BeautifulSoup
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.decorators import login_required   
from .models import wookname, groupies

# Create your views here.

reddit = praw.Reddit(client_id='wlJWUkwyl8E8UMx_V7WfVw', client_secret='cmVyaF4nfGdoAz7gW8LdNSsi6Zl2_g', user_agent='CommunityScrape')

def add(request):
    if  not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            add = form.cleaned_data['add']
            if not groupies.objects.filter(pookname= request.user, dagroup = add).exists():
                group1 = groupies(pookname= request.user, dagroup = add)
                group1.save()
        return redirect(request.META['HTTP_REFERER'])

def results(request):
    redinfo = ''
    quorainfo = ''
    facebook = ''
    redlink = False
    form = CommForm()
    form2 = AddForm()
    if request.method == 'POST':
        form = CommForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            facebook = f'https://www.facebook.com/groups/{name}'
            try:
                sub = reddit.subreddit(name)
                redinfo = sub.public_description
                redlink = f'https://reddit.com/r/{name}'
            except:
                redinfo = f'{name} is not a valid community'
            # Obaining Quora info
            URL = f'https://digg.com/{name}'
            form2.initial['add'] = redlink
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'lxml')
            quorainfo = soup.find("div").text
    return render(request, 'results.html', {
        'redlink': redlink,
        'redinfo': redinfo,
        'form2':form2,
        'form': form,
        'quorainfo': quorainfo
    })

def index(request):
    form = CommForm()
    return render(request, 'spoofed.html', {
        'form': form,
    })
def mygroups(request):
    group = groupies.objects.filter(pookname = request.user)
    RemoveFormSet = formset_factory(RemoveForm)
    if request.method == 'POST':
        formset = RemoveFormSet(request.POST)
        if formset.is_valid():
            for form in formset: 
                name = form.cleaned_data.get('remove')
                groupies.objects.filter(pookname = request.user, dagroup = name).delete()
        else:
            formset = RemoveFormSet()
    group = groupies.objects.filter(pookname = request.user)
    RemoveFormSet = formset_factory(RemoveForm, extra = groupies.objects.filter(pookname = request.user).count())
    formset = RemoveFormSet()
    for f,x in zip(formset,group): 
        f.initial['remove'] = x.dagroup
    return render(request, 'mygroups.html',{
        'formset': formset,
        'zip': zip(formset, group)
    })
def logout_view(request):
    logout(request)
    return redirect('/')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'login.html')

def create(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'create.html', {
        'form' : form
        })