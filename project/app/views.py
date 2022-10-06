from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import response
from rest_framework.response import Response
from rest_framework import views
from rest_framework import permissions
from rest_framework import status
from app.serializers import Pictures
from app.models import Picture

# Create your views here.
@api_view(['GET'])
def picture_list(request):
	pic = Picture.objects.all()
	serializer = Pictures(pic, many=True)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def pictures_detail(request, pk):
	pictures = Picture.objects.get(id=pk)
	try:
		serializer = Pictures(pictures)
		return Response(serializer.data)
	except:
		return Response(content={'message': 'The pictures does not exist'}, status=status.HTTP_404_NOT_FOUND)

	
@api_view(['DELETE'])
def pictures_detail(request, pk):
	pictures = Picture.objects.filter(id=pk).delete()
	try:
		serializer = Pictures(pictures)
		return Response(serializer.data)
	except:
		return Response(content={'message': 'The picture does not exist'}, status=status.HTTP_404_NOT_FOUND)

