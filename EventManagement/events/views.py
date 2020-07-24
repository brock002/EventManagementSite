from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from events.models import *
from events.forms import *
from django.db.models import Count

User=get_user_model()

# Create your views here.

# function based views

def index(request):
    return HttpResponseRedirect(reverse("events:events_list"))

def events_list(request, pk=1):
    city = City.objects.get(pk=pk)
    cat_ids = Category.objects.values_list("id", "name")
    event_list = Event.objects.filter(city=city)
    event_list = event_list.annotate(follower_count=Count("follower"))
    events_by_city={}
    for num, name in cat_ids:
        events_by_city[num]=event_list.filter(category__id=num).order_by("-follower_count")[:10]
    return render(request, "events/events_list.html", {"city":city, 'category_ids':cat_ids, 'events_dict':events_by_city, 'cities_list':City.objects.all()})

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    city = event.city
    address = event.address
    # address = address.replace(', ', '%2C')
    address = address.replace(',', '%2C')
    address = address.replace(' ', '%20')

    try:
        user = User.objects.get(pk=request.user.pk)
        follower = Follower.objects.get(event=event, follower=user)
    except:
        return render(request, "events/event_detail.html", {'event':event, 'city':city, 'address':address})
    else:
        return render(request, "events/event_detail.html", {'event':event, 'city':city, 'address':address, 'follow':True})   

def search_view_for_strings(request, city_pk, sr_string='', filter=''):
    from django.utils import timezone
    current = timezone.now().date().isocalendar()
    city = City.objects.get(pk=city_pk)
    event_list = Event.objects.filter(city=city)
    if request.method == "POST":
        search_string = request.POST.get('string')
        event_list = event_list.filter(name__contains=search_string)
        return render(request, 'events/search.html', {'events':event_list, 'city':city, 'sr_string':search_string})
    if sr_string!='':
        event_list = event_list.filter(name__contains=sr_string)
        if filter!="":
            if filter=='month':
                event_list = event_list.filter(start_date__year=current[0], start_date__month=timezone.now().month)
            elif filter=='week':
                event_list = event_list.filter(start_date__year=current[0], start_date__week=current[1])
        return render(request, 'events/search.html', {'events':event_list, 'city':city, 'sr_string':sr_string})

def search_view_for_categories(request, city_pk, category_pk, filter='', dumb=0):
    from django.utils import timezone
    current = timezone.now().date().isocalendar()
    city = City.objects.get(pk=city_pk)
    event_list = Event.objects.filter(city=city)
    category = Category.objects.get(pk=category_pk)
    event_list = event_list.filter(category=category)
    if filter!="":
        if filter=='month':
            event_list = event_list.filter(start_date__year=current[0], start_date__month=timezone.now().month)
        elif filter=='week':
            event_list = event_list.filter(start_date__year=current[0], start_date__week=current[1])
    return render(request, 'events/search.html', {'events':event_list, 'city':city, 'category':category, 'filtered':filter})

@login_required
def follow_event(request, pk):
    user = User.objects.get(pk=request.user.pk)
    event = Event.objects.get(pk=pk)
    try:
        follower = Follower.objects.get(event=event, follower=user)
    except:
        follower = Follower(event=event, follower=user)
        follower.save()
    else:
        follower.delete()
    finally:
        return HttpResponseRedirect(reverse_lazy('events:event_detail', kwargs={"pk":pk}))


# class based views

class CreateEvent(CreateView, LoginRequiredMixin):
    form_class = CreateEventForm
    model = Event

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.organiser = self.request.user
        self.object.save()
        return super().form_valid(form)


class EventUpdateView(UpdateView, LoginRequiredMixin):
    model = Event
    form_class = UpdateEventForm

class CreateEventImages(CreateView, LoginRequiredMixin):
    form_class = EventImageForm
    model = EventImage

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.event = Event.objects.get(pk=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)


class UpdateEventImages(UpdateView, LoginRequiredMixin):
    model = EventImage
    form_class = EventImageForm


# function based view for event creation:
# @login_required
# def create_event(request):
#     form = CreateEventForm()
#     if request.method == "POST":
#         form = CreateEventForm(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.organiser = User.objects.get(pk=request.user.pk)
#             event.save()
#             return HttpResponseRedirect(reverse_lazy('events:event_detail', kwargs={"pk":event.pk}))
#     return render(request, 'events/event_form.html', {'form':form})

# function for browse all in user following events(complete waste)
# def user_follows(request):
#     events_list = []
#     for follow in Follower.objects.filter(follower=request.user):
#         events_list.append(follow.event)

#     return render(request, 'events/search.html', {'events':events_list, 'follow':True})