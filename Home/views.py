from django.shortcuts import render , HttpResponse
from Home.models import Sell
# Create your views here.
def index(request):
    products=Sell.objects.all()  # This line is not necessary unless you want to fetch all Sell objects
    context = {
        'products': products
    }
    return render(request, 'hello.html', context)
    # return HttpResponse("Hello, this is the Home page of the Django project.")
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')
def sell(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_age = request.POST.get('product_age')
        product_discription = request.POST.get('product_discription')
        product_price = request.POST.get('product_price')
        contact = request.POST.get('contact')
        product_file = request.FILES['product_image']
        sell = Sell(product_name=product_name, product_age=product_age, product_discription=product_discription,contact=contact ,product_price=product_price, product_file=product_file)
        sell.save()

    return render(request, 'sell.html')

    # return HttpResponse("Hello, this is the about page of the Django project.")