from django.shortcuts import render

# Create your views here.
def vel(request):
    return render(request,'vels.html')
