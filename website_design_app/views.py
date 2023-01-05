from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'website_design_app/index.html')
