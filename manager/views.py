from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View

from .forms import CreateTrans
from .models import Transactions, Categories

# Create your views here.
def transaction_list(request):
    transaction = Transactions.objects.all()
    summ = 0
    for trans in transaction:
        summ+=trans.total
    return render(request, 'manager/transaction_list.html', context={'content': transaction, 'summ':summ})

def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'manager/categories_list.html', context ={'categories': categories})
def category_details(request, slug):
    category = get_object_or_404(Categories, slug__iexact= slug)
    return render(request, 'manager/category_details.html', context={'category': category})
def transaction_details(request, slug):
    transaction = get_object_or_404(Transactions, slug__iexact= slug)
    return render(request, 'manager/transaction_details.html', context={'transaction': transaction})
def show_cats(request, slug):
    cat= get_object_or_404(Categories, slug__iexact= slug)
    transaction = Transactions.objects.filter(category_id=cat.pk)
    summ = 0
    for trans in transaction:
        summ+=trans.total
    context = {'content': transaction, 'summ': summ, 'cat_selected': cat.pk}
    return render(request, 'manager/transaction_list.html', context=context)
class TransactionCreate(View):
    def get(self, request):
        form = CreateTrans()
        return render(request, 'manager/transaction_create.html',context={'form':form})

    def post(self, request):
        form = CreateTrans(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                #bound_form=Transactions.objects.create(**form.cleaned_data)
                form.save()
                return redirect('transaction_url')
                # return redirect('transaction_details_url', slag=bound_form.slug)
            except:
                form.add_error(None,"ERROR add new transaction")

        # else: form = CreateTrans()
            # return redirect('transaction_url')


        return render(request, 'manager/transaction_create.html', context={'form': form})
