from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import Test,User
from .serializers import TestSerializer, UserSerializer, ResultSerializer

class UserRegistrationView(APIView):
    # register user
    def post(self, request:Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f"Welcom to our site!!! You have successfully registered!!!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # get user 
    def get(self, request:Request, pk:int=None):
        if pk!=None:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response("this user does not exist",status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
class TestView(APIView):
    permission_classes  = [IsAuthenticated]
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
    
    # post method 
    def post(self, request:Request):
        data = request.data
        serializer = TestSerializer(data=data)
        question = data["question_str"]
        print(request.user)
        find = Test.objects.filter(question_str = question )
        print(len(find))
        
        if serializer.is_valid():
            if find==0 and request.user == 'admin':
                serializer.save()
                return Response("Congrulations this test add baza!!!",status=status.HTTP_201_CREATED)
            elif find != 0 and  request.user =='admin':
                return Response("this test already exist", status=status.HTTP_208_ALREADY_REPORTED)
            elif request.user !='admin':
                return Response("You cannot create a test!!!", status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# result class 
class ResultView(APIView):
    pass


