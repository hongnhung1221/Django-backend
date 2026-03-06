from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from base.models import Product 
from base.products import products

class Command(BaseCommand):
    help = 'Tu dong tao tai khoan Admin'

    def handle(self, *args, **options):
        username = 'ad'
        email = 'ad2@gmail.com'
        password = '887675nh'
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Da tao Admin thanh cong: {username}'))
        else:

            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Da cap nhat mat khau cho Admin: {username}'))
        
        

        for p in products:
            if not Product.objects.filter(name=p['name']).exists():
                Product.objects.create(
                    name=p['name'],
                    price=p['price'],
                    countInStock=p['countInStock'],
                    description=p['description'] ,
                    rating=p['rating'],
                    image=p['image'],
                    brand=p['brand'],
                    category=p['category'],
                    numReviews=p['numReviews'],
                )
        self.stdout.write(self.style.SUCCESS('Da import xong products tu file products.py!'))