from contact.forms import SubscribeForm

def subscribe_form(request):
    form = SubscribeForm()
    return {'subscribe_form': form}