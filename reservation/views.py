from django.shortcuts import render, get_object_or_404, redirect, reverse

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseRedirect, Http404
from django.utils.translation import ugettext_lazy as _

from .models import Reservation
from .forms import ReservationForm


class ReservationList(ListView):
    model = Reservation
    paginate_by = 10
    template_name = 'reservation/reservation_list.html'


# class ReservationCreate(CreateView):
#     model = Reservation
#     fields = ['user', 'start_date', 'end_date', 'people']
#     template_name = 'reservation/reservation_create.html'
#     success_url = '/'
#
#     def form_valid(self, form):
#         # 입력된 자료가 올바른지 채크
#         if form.is_valid():
#             # 올바르다면
#             # form : 모델 폼
#             form.instance.save()
#             return redirect('/')
#         else:
#             # 올바르지 않다면
#             return self.render_to_response({'form':form})

def reservation_create(request):
    if request.method == "POST":
        # 처리
        # request.POST : 폼에서 입력한 텍스트 데이터
        # request.FILES : 파일 데이터
        form = ReservationForm(request.POST, request.FILES)  # 데이터가 있는 form

        if form.is_valid():
            reservation = form.save()
            return redirect(reverse('reservation:detail', args=[reservation.id]))
    else:
        form = ReservationForm()
        # 입력 창 Form
    return render(request, 'reservation/reservation_create.html', {'form': form})


# class ReservationUpdate(UpdateView):
# #     model = Reservation
# #     fields = ['user', 'start_date', 'end_date', 'people']
# #     template_name = 'reservation/reservation_update.html'
# #     success_url = '/'


def reservation_update(request, reservation_id):
    if request.method == "POST":
        reservation = Reservation.objects.get(pk=reservation_id)
        form = ReservationForm(request.POST, request.FILES, instance=reservation)  # 데이터가 있는 form

        if form.is_valid():
            reservation = form.save()
            return redirect(reservation)
    else:
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation/reservation_update.html', {'form': form})


class ReservationDelete(DeleteView):
    model = Reservation
    template_name = 'reservation/reservation_delete.html'
    success_url = '/'


class ReservationDetail(DetailView):
    model = Reservation
    template_name = 'reservation/reservation_detail.html'