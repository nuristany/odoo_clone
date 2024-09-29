
from rest_framework.views import APIView
from . serializers import OTPVerificationSerializer
from rest_framework.response import Response
from rest_framework import generics, status



class OtpVerificationView(APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            





