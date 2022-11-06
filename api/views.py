from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["GET"])
def home_view(request):
	model_obj = Product.objects.all().order_by('?').first()
	data = {}
	if model_obj:
		# data['id'] = model_obj.id
		# data['title'] = model_obj.title
		# data['details'] = model_obj.details
		# data['price'] = model_obj.price

		data = model_to_dict(model_obj)
	return Response(data)