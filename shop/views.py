from django.shortcuts import render, redirect
from django.views import View
from. models import Category
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from shop.forms import SignupForm , LoginForm , CategoryForm, ProductForm, StockForm
from shop.models import Product

# Create your views here.

class Categories(View):
    def get(self, request):
        c=Category.objects.all()
        context = {'categories': c}
        return render(request, 'categories.html',context)
    
class Register(View):
    
    def post(self, request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()

            return redirect('shop:login')
    
    def get(self,request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request, 'register.html', context)
    

class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('shop:categories')
            else:
                messages.error(request, "Invalid username or password")

        return render(request, 'login.html', {'form': form})


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('shop:login')
    
class Products(View):
    def get(self,request, i):
        c=Category.objects.get(id=i)
        context = {'category':c}
        return render (request,'products.html',context)
    

class AddCategory(View):
    
    def post(self,request):
        form_instance = CategoryForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')

    def get(self,request):
        form_instance = CategoryForm()
        context = {'form':form_instance}
        return render(request, 'addcategory.html', context)
    

class AddProduct(View):
    
    def post(self,request):
        form_instance = ProductForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')

    def get(self,request):
        form_instance = ProductForm()
        context = {'form':form_instance}
        return render(request, 'addproduct.html', context)
    
class ProductDetail(View):
    def get(self, request, i):
        p = Product.objects.get(id=i)    
        context = {'product': p}
        return render(request, 'productdetail.html', context)
    

class EditStock(View):
    
    def get(self, request, i):
        p = Product.objects.get(id=i)
        form_instance = StockForm(instance=p)
        return render(request, 'editstock.html', {'form': form_instance})

    def post(self, request, i):
        p = Product.objects.get(id=i)
        form_instance = StockForm(request.POST, instance=p)
        
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')
        
        return render(request, 'editstock.html', {'form': form_instance})


