from django.shortcuts import render

# Create your views here.
def method1(request):
    return render(request,'parent.html')

def method2(request):
    return render(request,'child.html')