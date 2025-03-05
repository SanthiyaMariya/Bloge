from django.core.management.base import BaseCommand
from bloge.models import Category
from bloge.models import Hotel

class Command(BaseCommand):

     help="this comamnd insert post data into database"
     
     def handle(self, *args, **options):
         

         Category.objects.all().delete()

         category=['art',
               'technology',
               'science',
               'AI',
               'tools'
               ]

         for catogery_name in category:
              Category.objects.create(name=catogery_name)
      
         self.stdout.write(self.style.SUCCESS('data added successfuly'))








 