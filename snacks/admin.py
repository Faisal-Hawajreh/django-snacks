from django.contrib import admin
from .models import Snack , SpicySnack


# Register your models here.
@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    pass

@admin.register(SpicySnack)
class AdminSpicySnack(admin.ModelAdmin):
    list_display = ['name', 'price' , 'spicy' ]