from django.shortcuts import render
from django.http import HttpResponse
import rollbar

def index(request):
    return render(
        request,
        "index.html",
    )



def rollbar_test(request):
    try:
        a = None
        a.hello()
    except Exception:
        rollbar.report_exc_info()
        raise

