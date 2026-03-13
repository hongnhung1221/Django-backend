from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from base.models import Product 
from base.products import products

class Command(BaseCommand):
    # help = 'Tu dong tao tai khoan Admin'

    def handle(self, *args, **options):
        # username = 'ad'
        # email = 'ad6@gmail.com'
        # password = '887675nh'
        
        # if not User.objects.filter(username=username).exists():
        #     User.objects.create_superuser(username, email, password)
        #     self.stdout.write(self.style.SUCCESS(f'Da tao Admin thanh cong: {username}'))
        # else:

        #     user = User.objects.get(username=username)
        #     user.set_password(password)
        #     user.is_staff = True
        #     user.is_superuser = True
        #     user.save()
        #     self.stdout.write(self.style.SUCCESS(f'Da cap nhat mat khau cho Admin: {username}'))
        
        

        for p in products:
            obj, created = Product.objects.update_or_create(
                name=p['name'], 
                defaults={
                    'price': p['price'],
                    'countInStock': p['countInStock'],
                    'description': p['description'],
                    'rating': p['rating'],     
                    'numReviews': p['numReviews'], 
                    'image': p['image'],
                    'brand': p['brand'],
                    'category': p['category'],
                }
            )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Da tao moi: {p['name']}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Da cap nhat: {p['name']}"))