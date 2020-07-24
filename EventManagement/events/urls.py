"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

app_name = 'events'

urlpatterns = [
    path('in/<int:pk>/', views.events_list, name='events_list'),
    path('in/default/', views.events_list, name='events_list'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('<int:pk>/follow/', views.follow_event, name='follow_event'),
    path('create/', views.CreateEvent.as_view(), name='create_event'),
    path('update/<int:pk>', views.EventUpdateView.as_view(), name='update_event'),
    path('add/images/<int:pk>', views.CreateEventImages.as_view(), name='create_event_images'),
    path('edit/images/<int:pk>', views.UpdateEventImages.as_view(), name='update_event_images'),
    
    # strings search view links
    path('search/<int:city_pk>', views.search_view_for_strings, name='search_strings'),
    path('search/<int:city_pk>/<str:sr_string>/filter/by/this/<str:filter>', views.search_view_for_strings, name='search_strings'),

    # categories search view links
    path('search/<int:city_pk>/<int:category_pk>', views.search_view_for_categories, name='search_categories'),
    path('search/<int:city_pk>/<int:category_pk>/filter/by/this/<str:filter>/<int:dumb>', views.search_view_for_categories, name='search_categories'),

    # path('your/follows', views.user_follows, name='user_follows'), url for browse all button in user following events
]