# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Appointment
from datetime import datetime

@api_view(['GET'])
def get_available_slots(request):
    date = request.GET.get('date')
    if not date:
        return Response({'error': 'Date parameter is required'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    booked_appointments = Appointment.objects.filter(date=date)
    booked_slots = [apt.time for apt in booked_appointments]

    return Response({'booked_slots': booked_slots})

@api_view(['POST'])
def create_appointment(request):
    try:
        name = request.data.get('name')
        phone = request.data.get('phone')
        date = request.data.get('date')
        time = request.data.get('time')

        if not all([name, phone, date, time]):
            return Response({'error': 'All fields are required'},
                          status=status.HTTP_400_BAD_REQUEST)

        appointment = Appointment.objects.create(
            name=name,
            phone=phone,
            date=date,
            time=time
        )
        
        return Response({
            'id': appointment.id,
            'name': appointment.name,
            'date': appointment.date,
            'time': appointment.time
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, 
                       status=status.HTTP_400_BAD_REQUEST)