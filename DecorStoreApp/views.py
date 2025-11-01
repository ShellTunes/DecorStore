from django.shortcuts import render
from django.http import JsonResponse
from .models import Transporter
# Create your views here.
def get_transporter_contact(request):
    transporter_id = request.GET.get('id')
    if transporter_id:
        try:
            transporter = Transporter.objects.get(id=transporter_id)
            return JsonResponse({"contactnumber": transporter.Phone}, status=200)
        except Transporter.DoesNotExist:
            return JsonResponse({"error": "Transporter not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)