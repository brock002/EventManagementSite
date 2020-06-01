from django.contrib import admin
from events.models import Category, City, Event, Follower
# Register your models here.

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Event)
admin.site.register(Follower)