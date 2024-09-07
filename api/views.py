from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer

class Api(APIView):
    def post(self,request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('this is data succese fully save....', { 'data':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self,request):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates ,many = True)
        
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
        

