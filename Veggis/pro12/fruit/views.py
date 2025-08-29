from django.shortcuts import render
import requests

def home(request):
    d = requests.get("https://fakestoreapi.com/products")
    print(d)
    d = d.json()
    dataobj = [data for data in d]
    return render(request, 'cart.html',context={'data':dataobj})

def shop(request):
    return render(request, 'shop.html')
def shop_details(request):
    return render(request, 'shop_details.html')

def checkout(request):
    return render(request,'chackout.html')

def manage(request):
    return render(request,'index.html')

def test(request):
    return render(request,'testimonil.html')

def contact(request):
    return render(request,'contact.html')

