from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'ashu','age':3}
    return render (request,'jinja_printing.html',context=d)