from django.shortcuts import render
from .forms import UploadForm,ProfileUpdateForm
from .models import Image, Profile, Comments
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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
    current_profile=Profile.objects.exclude(id=request.user.id)
    users_posts=Image.objects.filter(user=request.user)[::-1]
    if request.method == "POST":
        profile_update=ProfileUpdateForm(request.POST, request.FILES)
        # import pdb; pdb.set_trace()
        if profile_update.is_valid():
            updated = profile_update.save(commit=False)
            updated.user = request.user
            updated.save()
            return HttpResponseRedirect(request.path_info)
    else:
        profile_update=ProfileUpdateForm()
    context={
        'users_posts':users_posts,
        'update_form':profile_update,
        'user':current_profile,
    }
    return render(request, 'profile.html', context)
