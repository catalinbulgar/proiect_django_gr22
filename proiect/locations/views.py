from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView

from locations.models import Location


class CreateLocationView(CreateView):
    model = Location
    template_name = 'forms.html'
    fields = ['city', 'country']

    def get_success_url(self):
        return reverse('locations:adaugare')
