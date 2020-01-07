from django.shortcuts import render
from .forms import UploadForm
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
            upload.user = request.user.profile
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
    pass
