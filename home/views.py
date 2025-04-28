from django.shortcuts import render

# Create your views here.
def coming_soon(request):
    return render(request, 'views/coming-soon.html')