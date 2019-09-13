from django.shortcuts import render
def index(request):
    # View code here...
    return render(request, 'dashboard/index.html')

def detail(request):
    return HttpResponse("You're looking at question")