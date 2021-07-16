from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Transactions, Categories

# Create your views here.
def transaction_list(request):
    transaction = Transactions.objects.all()
    return render(request, 'manager/transaction_list.html', context={'content': transaction})

def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'manager/categories_list.html', context ={'categories': categories})
def category_details(request, slug):
    category = get_object_or_404(Categories, slug__iexact= slug)
    return render(request, 'manager/category_details.html', context={'category': category})
