from django.shortcuts import render

# Create your views here.
def base_page(request):
    return render(request,'institute_management/base.html')

def index_page(request):
    return render(request,'institute_management/index.html')

def login_page(request):
    return render(request,'institute_management/login.html')
