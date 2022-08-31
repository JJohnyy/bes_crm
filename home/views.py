from django.shortcuts import render

# Create your views here.


def home(request):
    ''' view to render a home page '''
    return render(request, 'home/home.html')



