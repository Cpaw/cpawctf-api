from django.contrib import admin
from .models import *

@admin.register(Player)
class Player(admin.ModelAdmin):
    pass

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

@admin.register(Challenge)
class Challenge(admin.ModelAdmin):
    pass

@admin.register(Notice)
class Notice(admin.ModelAdmin):
    pass


