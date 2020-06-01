from django import forms
from events.models import Event, EventImage

class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ['organiser', 'notice']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            'start_date': forms.SelectDateWidget,
            'address': forms.TextInput(attrs={'placeholder':"e.g.-Rabindra Bhawan, Ambari, Guwahati"}),
        }
        labels = {
            'name': ('Event Name'),
            'address': ('Full Address/Location'),
            'start_date': ('Date'),
        }
        help_texts = {
            'description': ('Enter full details about your Event in Description. Including:<br> 1. Time and duration information.<br>2. Contact info such as email address and phone number of you or any other co-ordinator'),
            'start_date': ('<li>Enter only the Start Date here.</li><li>Put the rest of the Time information inside description.</li>'),
            'category': ('<li>You can\'t edit this later</li>'),
            'address': ('<li>Try to put it in google map searchable terms</li><li>Any extra information you may want to add should go inside description</li>'),
        }

class UpdateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'description', 'start_date', 'address')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            'start_date': forms.SelectDateWidget,
            'address': forms.TextInput(attrs={'placeholder':"e.g.-Rabindra Bhawan, Ambari, Guwahati"}),
        }
        labels = {
            'name': ('Event Name'),
            'address': ('Full Address/Location'),
            'start_date': ('Date'),
        }
        help_texts = {
            'description': ('Enter full details about your Event in Description. Including:<br> 1. Time and duration information.<br>2. Contact info such as email address and phone number of you or any other co-ordinator'),
            'start_date': ('<li>Enter only the Start Date here.</li><li>Put the rest of the Time information inside description.</li>'),
            'address': ('<li>Try to put it in google map searchable terms</li><li>Any extra information you may want to add should go inside description</li>'),
        }

class EventImageForm(forms.ModelForm):

    class Meta:
        model = EventImage
        exclude = ['event']

