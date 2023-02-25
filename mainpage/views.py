from django.shortcuts import render

# Create your views here.
def mainpageaction(request):
    context = {'message' : 'Hello, World'}
    return render(request, 'mainpage.html', context)
    

