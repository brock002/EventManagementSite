from django.contrib import admin
from events.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Event)
admin.site.register(Follower)
admin.site.register(EventImage)