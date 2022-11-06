from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["GET"])
def home_view(request):
	instance = Product.objects.all().order_by('?').first()
	data = {}
	if instance:

		# WAY 1

		# data['id'] = instance.id
		# data['title'] = instance.title
		# data['details'] = instance.details
		# data['price'] = instance.price

		# WAY 2

		# data = model_to_dict(instance)

		# WAY 3

		data = ProductSerializer(instance).data
	return Response(data)