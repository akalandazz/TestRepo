from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from ..models import Shifts, MorningShift, MiddayShift, NightShift, Person
from .serializers import ShiftSerializer, MorningShiftSerializer, MiddayShiftSerializer, NightShiftSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class ShiftsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer


class MorningShiftViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MorningShift.objects.all()
    serializer_class = MorningShiftSerializer


class MiddayShiftViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =MiddayShift.objects.all()
    serializer_class = MiddayShiftSerializer



class NightShiftViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  NightShift.objects.all()
    serializer_class =  NightShiftSerializer




class ShiftEnrollView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, name, format=None):
        shift = get_object_or_404(MorningShift, pk=pk)
        if shift.on_duty:
            if shift.on_duty.pk == request.user.pk:
                return Response({'enrolled': False,'text':"You are already enrolled"})
        else:
            person = get_object_or_404(Person, name=name)
            shift.on_duty = person
            shift.save()
            return Response({'enrolled': True})