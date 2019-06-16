from django.shortcuts import render

def anlgClock(request):
    return render(request, 'clock/mainhome.html')


def nextpage(request):
    return render(request, 'clock/index.html')