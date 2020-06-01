from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True)
    notice = models.CharField(null=True, max_length=50, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('events:event_detail', kwargs={'pk': self.pk})

class Follower(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.follower.username+" follows "+self.event.name

class EventImage(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='event_image_one', blank=True)
    image2 = models.ImageField(upload_to='event_image_two', blank=True)
    image3 = models.ImageField(upload_to='event_image_three', blank=True)
    image4 = models.ImageField(upload_to='event_image_four', blank=True)
    image5 = models.ImageField(upload_to='event_image_five', blank=True)
    
    def __str__(self):
        return self.event.name+"'s images"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('events:event_detail', kwargs={'pk': self.event.pk})