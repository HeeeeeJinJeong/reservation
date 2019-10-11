from django.shortcuts import render, get_object_or_404, redirect, reverse

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseRedirect, Http404
from django.utils.translation import ugettext_lazy as _

from .models import Reservation
from .forms import ReservationForm, ReservationPasswordForm


class ReservationList(ListView):
    model = Reservation
    paginate_by = 10
    template_name = 'reservation/reservation_list.html'


class ReservationCreate(CreateView):
    model = Reservation
    fields = ['user', 'start_date', 'end_date', 'people']
    template_name = 'reservation/reservation_create.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        form = ReservationForm()
        if request.POST:
            return render(request, self.template_name)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation:list')
        return self.render_to_response({'form': form})


class ReservationUpdate(UpdateView):
    model = Reservation
    fields = ['user', 'start_date', 'end_date', 'people', 'password']
    template_name = 'reservation/reservation_update.html'
    success_url = '/'


class ReservationDelete(DeleteView):
    model = Reservation
    template_name = 'reservation/reservation_delete.html'
    success_url = '/'


class ReservationDetail(DetailView):
    model = Reservation
    template_name = 'reservation/reservation_detail.html'

    def get(self, request, *args, **kwargs):
        form = ReservationPasswordForm()
        if request.POST:
            return render(request, self.template_name)
        object = self.get_object()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args,**kwargs):
        object = self.get_object()
        form = ReservationPasswordForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == object.password:
                # form = AppointmentPasswordForm(request.POST)
                return render(request, self.template_name,{'object': object})

        return render(request, self.template_name, {'form': form})