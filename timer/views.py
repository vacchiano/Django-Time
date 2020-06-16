from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    nowTime = datetime.now()
    strCurrentTime = nowTime.strftime('%H:%M:%S')
    context = {
        "time" : strCurrentTime
    }
    # render the template
    return render(request, "index.html", context)