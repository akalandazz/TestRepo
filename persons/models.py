from django.db import models
from datetime import datetime, time


class Person(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length= 60)

    def __str__(self) -> str:
        return f"User {self.name}"



class ShiftBase(models.Model):
    title = models.CharField(max_length= 70)
    slug = models.SlugField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    date = models.DateField(null=True)

    @property
    def shift_duration(self):
        t1 = datetime.strptime(str(self.start_time), '%H:%M:%S')
        t2 = datetime.strptime(str(self.end_time), '%H:%M:%S')
        dt = abs(t2 - t1)
        return time(dt.seconds // 3600, (dt.seconds // 60) % 60).strftime('%H:%M')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.title}"

class MorningShift(ShiftBase):
    on_duty = models.ForeignKey(Person, on_delete=models.CASCADE,blank=True, null=True, related_name="person_moning_shifts")

class MiddayShift(ShiftBase):
    on_duty = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, related_name="person_midday_shifts")

class NightShift(ShiftBase):
    on_duty = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, related_name="person_night_shifts")



class Shifts(models.Model):
    title = models.CharField(max_length= 70)
    morning = models.ForeignKey(MorningShift, on_delete=models.CASCADE,blank=True, null=True, related_name="morning_shifts",)
    midday = models.ForeignKey(MiddayShift, on_delete=models.CASCADE,blank=True, null=True, related_name="midday_shifts")
    night = models.ForeignKey(NightShift, on_delete=models.CASCADE, blank=True, null=True, related_name="night_shifts")


    def __str__(self) -> str:
        return f"{self.title}"


