from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact
from math import ceil


def index(request):
    # products = Product.objects.all()
    # print(products)
    #n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    # params = {'no_of_slides':nSlides, 'range': range(1, nSlides), 'product':   products}
    #allProds = [[products, range(1, nSlides), nSlides],
    #           [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'EventManagement/index.html',
                  params)

def about(request):
    return render(request, 'EventManagement/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'EventManagement/contact.html')

def tracker(request):
    return render(request, 'EventManagement/tracker.html')

def search(request):
    return render(request, 'EventManagement/search.html')

def productView(request, myid):
    product = Product.objects.filter(id=myid)

    return render(request, 'EventManagement/productview.html', {'product':product[0]})

def checkout(request):
    return render(request, 'EventManagement/checkout.html')