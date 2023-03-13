from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Info_1
# Create your views here.

class data(CreateView):
    template_name = 'create.html'
    model = Info_1
    fields = '__all__'
    success_url = 'create'

class update_1(UpdateView):
    template_name = 'update.html'
    model = Info_1
    fields = ['Name','Mobile_no']
    success_url = 'update'

class delete_1(DeleteView):
    template_name = 'delete.html'
    model = Info_1
    fields = '__all__'
    success_url = '/create'