from django.shortcuts import redirect

def redirect_FM(request):
    return redirect('transaction_url',permanent=True)