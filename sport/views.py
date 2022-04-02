from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect

# Create your views here.
def index_view(request):

    return render(request,"sport/index.html")