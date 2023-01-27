from django.contrib import admin

from .models import Food, Donators

admin.site.register(Food)
# Register your models here.
#add to database without form
#can delete a user 


admin.site.register(Donators)
