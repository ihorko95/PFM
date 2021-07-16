from django.shortcuts import redirect

def redirect_FM(request):
    return redirect('manager_url',permanent=True)