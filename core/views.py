from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import *
from .models import Profile, TutorialVideo, FAQ

def Frontend(request):
	return render(request, "index.html")

class RegisterUser(APIView):

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = Register(data = data)

		if serializer.is_valid(raise_exception = True):
			user = serializer.save()
			return Response(serializer.data, status = status.HTTP_200_OK)

		return Response(serializer.errors, status = status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetUser(request):
	username = request.user.username

	return Response({"username": username})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetProfile(request):
	user = request.user
	profile = user.profile

	serializer = ProfileSerializer(user)
	return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def SetProfile(request):
	user = request.user
	Profile.objects.create(
		dob = request.data.get('dob'),
		height = request.data.get('height'),
		weight = request.data.get('weight'),
		physique = request.data.get('physique'),
		payment_status = 'not_paid',
		user = user
	)
	return Response({"message": "Profile Created Successfully"}, status = status.HTTP_200_OK)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def Pay(request):
	user = request.user

	user.profile.payment_status = 'pending'
	user.save()
	return Response({"message": "Payment pending"}, status = status.HTTP_200_OK)

@api_view(["GET"])
def GetAllTutorials(request):
	videos = list(TutorialVideo.objects.values('id', 'title', 'description', 'video_id'))

	return JsonResponse(videos, safe = False)	

@api_view(["GET"])
def GetOneTutorial(request):
	video_id = request.data.get('id')
	video = get_object_or_404(User, id = video_id)

	serializer = TutorialSerializer(video)

	return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getFAQs(request):
	faqs = list(FAQ.objects.values('question', 'answer'))

	return JsonResponse(faqs, safe = False)

@api_view(["GET"])
def getFAQ(request):
	faq_id = request.data.get('id')
	faq = get_object_or_404(FAQ, id = faq_id)
	serializer = FAQParser(faq)

	return Response(serializer.data, status = status.HTTP_200_OK)