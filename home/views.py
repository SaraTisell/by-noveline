from django.shortcuts import render


def index(request):
    """ View to return index page """
    return render(request, 'home/index.html')

def privacy_policy(request):
    """ View to render privacy policy """
    return render(request, 'home/privacy_policy.html')