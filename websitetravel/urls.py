"""websitetravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
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
from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Hotel, Rooms
from forms import HotelForm, RoomForm
from views import Create, DCreate, HotelDetail, review

urlpatterns = [

    url(r'\^\$',
        ListView.as_view(
        	queryset=Hotel.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
        	context_object_name='latest_restaurant_list',
        	template_name='myhotels/task2.html'),
        name='hotel_list'),


    url(r'\^hotels/(?P<pk>\d+)/\$',
        HotelDetail.as_view(),
        name='hotel_detail'),



# Create a restaurant, /myrestaurants/restaurants/create/
    url(r'\^restaurants/create/\$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

# Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'\oasistravels/(?P<pk>\d+)/edit/\$',
        UpdateView.as_view(
        	model = Restaurant,
        	template_name = task2.html',
        	form_class = RestaurantForm),
        name='restaurant_edit'),

