from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	dob = models.DateField()
	height = models.PositiveIntegerField()
	weight = models.PositiveIntegerField()
	physique_options = [
		('mesomorph', 'Mesomorph'),
		('ectomorph', 'Ectomorph'),
		('endomorph', 'Endomorph')
	]
	physique = models.CharField(max_length = 9, default = 'mesomorph', choices = physique_options)
	status_choices = [
		('paid', 'Paid'),
		('pending', 'Pending'),
		('not_paid', 'Not Paid')
	]
	payment_status = models.CharField(max_length = 8, default = 'not_paid')
	user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "profile")

class TutorialVideo(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	video_id = models.CharField(max_length = 500)

class FAQ(models.Model):
	question = models.TextField()
	answer = models.TextField()