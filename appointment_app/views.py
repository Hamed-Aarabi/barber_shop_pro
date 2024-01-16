import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Appointment, BarberWorkingDay
from datetime import timedelta


class AppointmentView(View):
    def post(self, request):
        fullname = request.POST.get('bb-name')
        phone = request.POST.get('bb-phone')
        time = request.POST.get('bb-time')
        branch = request.POST.get('bb-branch')
        date = request.POST.get('bb-date')
        number = request.POST.get('bb-number')
        message = request.POST.get('bb-message')
        if fullname and date and time and phone and branch and number:
            try:
                work_day = BarberWorkingDay.objects.get(work_date=date)
                user_time = datetime.datetime.strptime(time, "%H:%M")
                if user_time.time() >= work_day.start_at and user_time.time() <= work_day.end_at:
                    time_each_srvice = timedelta(minutes=work_day.time_each_service)
                    end_time = (user_time + time_each_srvice).time()
                    appointments = Appointment.objects.filter(book_date=date)
                    for appointment in appointments:
                        if user_time.time() >= appointment.book_time and user_time.time() <= appointment.end_time:
                            return JsonResponse({'message': 'duplicate'})

                    Appointment.objects.create(fullname=fullname, phone=phone, book_time=time, book_date=date,
                                               branch=branch,
                                               number_of_people=number, comment=message, end_time=end_time)
                    return JsonResponse({'message': 'Done'})
                else:
                    return JsonResponse({'message': 'out_time'})
            except BarberWorkingDay.DoesNotExist:
                return JsonResponse({'message': 'out_date'})
        return JsonResponse({'message': 'Error'})
