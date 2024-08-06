from django.shortcuts import render 

# Create your views here.
def get_hairstore_homepage(request):
    return render(request, 'hairstore/hairstore_list.html')