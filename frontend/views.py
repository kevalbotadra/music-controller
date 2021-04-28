from django.shortcuts import render

# Create your tests here.
def index(request, *args, **kwargs):
    return render(request, "frontend/index.html")