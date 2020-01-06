from django.shortcuts import render
from .forms import UploadForm
from .models import Image
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
##################from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts=Image.objects.all()[::-1]
    if request.method == "POST":
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload.save()
            HttpResponseRedirect('homePage')
    else:
        upload_form = UploadForm()
    return render (request, 'index.html',{"upload_form":upload_form, "posts":posts} )
