from django.shortcuts import render

"""connect data and templates, accept http requests and send send http answers"""

def index_page(request):
    return render(request, 'index.html')
