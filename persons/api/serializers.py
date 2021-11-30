from rest_framework import serializers
from ..models import Shifts, Person, MorningShift, MiddayShift, NightShift

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'surname']

class MorningShiftSerializer(serializers.ModelSerializer):
    on_duty = PersonSerializer()

    class Meta:
        model = MorningShift
        fields = ['id','title', 'slug', 'start_time', 'end_time', 'date','on_duty']


class MiddayShiftSerializer(serializers.ModelSerializer):
    on_duty = PersonSerializer()

    class Meta:
        model = MiddayShift
        fields = ['id','title', 'slug', 'start_time', 'end_time', 'date', 'on_duty']

class NightShiftSerializer(serializers.ModelSerializer):
    on_duty = PersonSerializer()

    class Meta:
        model = NightShift
        fields = ['id','title', 'slug', 'start_time', 'end_time', 'date', 'on_duty']


class ShiftSerializer(serializers.ModelSerializer):
    morning = MorningShiftSerializer()
    midday = MiddayShiftSerializer()
    night = NightShiftSerializer()
    class Meta:
        model = Shifts
        fields = ['id','title', 'morning', 'midday', 'night']

