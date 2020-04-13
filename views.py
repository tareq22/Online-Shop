from django.shortcuts import render

from django.http import HttpResponse
from dhango.shortcuts import get_object_or_404
from rest_framework.views APIView
from rest_framework.response import Response
from rest_framework import status
from . models import prolist
from . serializers import prolistSerializer

class prolisst(APIView):

    def get(self, request):
        prolist1= prolist.objects.all{}
        serializers=prolistSerializer(prolist1, many=True)
        return Response(serializer.data)



        def post(self):
            pass

