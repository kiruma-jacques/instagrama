from django.shortcuts import render
from .forms import UploadForm,ProfileUpdateForm
from .models import Image, Profile, Comments
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
##################from .email import send_welcome_email

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request,**kwargs):
    posts=Image.objects.all()[::-1]
    current_profile=Profile.objects.exclude(id=request.user.id)
    upload_form = UploadForm(request.POST, request.FILES)
    if request.method == "POST":
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload.user = request.user
            upload.save()
            return HttpResponseRedirect(request.path_info)
    else:
        upload_form = UploadForm()
    context ={
        'posts':posts,
        'form': upload_form,
        'user': current_profile,
    }
    return render (request, 'index.html',locals())

def profile(request):
    current_user = request.user
    current_profile = Profile.objects.get(user=request.user)
    users_posts = Image.objects.filter(user=request.user)[::-1]
    update_form = ProfileUpdateForm(request.POST, instance=request.user)
    if request.method == "POST":
        if update_form.is_valid():
            update = update_form.save(commit=False)
            update.user = current_user
            update.save
            return HttpResponseRedirect(request.path_info)
    else:
        update_form = ProfileUpdateForm()
    context={
        'user':current_user,
        'profile':current_profile,
        'posts':users_posts,
        'form':update_form,
    }
    return render(request, 'profile.html', locals())
