from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .emails import *
from .serializer import *


class RegisterAPI(APIView):
    def post(self, request):
        """try:
            data=request.data
            serializer=UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_otp_via_email(serializer.data['email'])
            return Response({
                "status": 200,
                "message": "registration successful please check mail",
                "data": serializer.data,
            })
        return Response({
            "status": 400,
            "message": "something went wong",
            "data": serializer.errors,
        })


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                        "status": 400,
                        "message": "something went wrong ",
                        "data": "invalid email",
                    })
                if not user[0].otp == otp:
                    return Response({
                        "status": 400,
                        "message": "something went wrong",
                        "data": "invalid otp",
                    })
                user[0].is_varified = True
                user[0].save()
                return Response({
                    "status": 200,
                    "message": "account verified",
                    "data": "serializer.data",
                })
            return Response({
                "status": 400,
                "message": "something went wrong",
                "data": serializer.errors,
            })





        except Exception as e:
            print(e)

from django.shortcuts import render
def index(request):
    return render(request,'index.html')