from django.db import models


class Appointment(models.Model):
    fullname = models.CharField(max_length=150)
    phone = models.CharField(max_length=16)
    branch = models.CharField(max_length=150)
    number_of_people = models.PositiveSmallIntegerField()
    book_date = models.DateField()
    book_time = models.TimeField()
    end_time = models.TimeField(null=True)
    comment = models.TextField(blank=True, null=True)
    book_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user: {self.fullname}. date:{self.book_date}. time:{self.book_time}'


class BarberWorkingDay(models.Model):
    work_date = models.DateField()
    start_at = models.TimeField()
    end_at = models.TimeField()
    start_rest_time = models.TimeField(blank=True, null=True)
    end_rest_time = models.TimeField(blank=True, null=True)
    time_each_service = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.work_date}'
