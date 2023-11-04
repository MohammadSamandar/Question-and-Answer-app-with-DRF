from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, Answer, Person
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import status
# Create your views here.

class QuestionView(APIView):

    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)




    def post(self, request):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass