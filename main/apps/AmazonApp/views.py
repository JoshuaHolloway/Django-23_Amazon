from django.shortcuts import render, redirect

from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, "AmazonApp/index.html")
    # return HttpResponse("hello")
