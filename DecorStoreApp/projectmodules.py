# # import jwt
# # from django.contrib.auth import get_user_model
# # from django.contrib.auth.signals import user_logged_in
# # from rest_framework.decorators import api_view, permission_classes
# # from rest_framework_jwt.serializers import jwt_payload_handler
# # from DecorStore import settings
# # from rest_framework.generics import RetrieveUpdateAPIView
# # from django.shortcuts import render
# # from rest_framework import generics, filters, status
# # from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import *
# # from django_filters.rest_framework import DjangoFilterBackend
# from datetime import *
# # import pytz
# # from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
# # from rest_framework.pagination import PageNumberPagination
# # from django.shortcuts import render, redirect
# # from django.http import JsonResponse
# # from django.views import View
# # from django.contrib.gis.geos import *
# # from django.contrib.gis.db import models
# # from django.contrib.gis.geos import Point, Polygon
# # from django.contrib.gis.measure import D
# # from geopy.distance import geodesic
# # from geopy.distance import great_circle
# # from rest_framework_jwt.settings import api_settings
# # from django.contrib import messages
# # from django.contrib.auth import authenticate
# # from django.conf import settings
# from rest_framework.parsers import MultiPartParser, FormParser
# # import stripe
# # import json
# # from django.core.validators import validate_email
# # from django.contrib.auth.hashers import make_password
# # import string
# # import random
# # import time
# from rest_framework.exceptions import APIException
# # from django.core.paginator import Paginator
# # from rest_framework.reverse import reverse
# # import requests
# # from pathlib import Path

# from math import radians, cos, sin, asin, sqrt
# # from geopy import distance


# error_msg = {
#     'error'		: True,
#     'message'	: 'Service temporarily unavailable, try again later'
# }


# class ServiceUnavailable(APIException):
#     status_code = 503
#     default_detail = 'Service temporarily unavailable, try again later.'
#     default_code = 'service_unavailable'
