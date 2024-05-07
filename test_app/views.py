from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from django.contrib.auth import hashers

from .models import Test,User, Result
from .serializers import TestSerializer, UserSerializer, ResultSerializer
from unittest import result


# login class :
class LoginView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request:Request)->Response:
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.get(username=username)
        if not user:
            return Response("You are not registered in the system or you entered the wrong username!!!", status=status.HTTP_401_UNAUTHORIZED) 
        else:               
            return Response('You are successfully logged in!!!', status=status.HTTP_202_ACCEPTED)
        

class UserRegistrationView(APIView):
    # register user
    def post(self, request:Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f"Welcom to our site!!! You have successfully registered!!!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # get user 
    def get(self, request:Request):
        username = request.user
        data = User.objects.get(username=username)
        return Response({
            'username': data.username,
            "first_name": data.first_name,
            "last_name": data.last_name,
            "email": data.email
            }, status=status.HTTP_202_ACCEPTED)
        
    
class TestView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    # permission_classes  = [IsAuthenticated]
    def get(self, request: Request, pk=None,q_type=None,q_subject=None) -> Response:
        if pk is None and q_subject is None and q_type is None:
            tests = Test.objects.all()
            serializer = TestSerializer(tests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif q_subject==None and q_type==None:
            try:
                test = Test.objects.get(pk=pk)
                serializer = TestSerializer(test)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif pk==None and q_subject==None:
            try:
                test = Test.objects.filter(question_type1=q_type)
                serializer = TestSerializer(test,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif pk==None:
            try:
                task = Test.objects.filter(question_type1=q_type,question_subject=q_subject)
                serializer = TestSerializer(task,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
    

# result class 
class ResultView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    # get method
    def get(self, request:Request, pk = None):
        if pk==None:
            restult = Result.objects.all()
            serializer = ResultSerializer(restult, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                result = Result.objects.get(pk = pk)
                serializer = ResultSerializer(result)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Result.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self, request:Request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



