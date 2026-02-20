from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('signup/', views.RegisterUser.as_view()),

	path('login/', TokenObtainPairView.as_view(), name = 'obtain-token'),
	path('login/refresh/', TokenRefreshView.as_view(), name = 'refresh-token'),

	path('get_user/', views.GetUser),
	path('getprofile/', views.GetProfile),
	path('setprofile/', views.SetProfile),
	path('pay/', views.Pay),
	path('get_all_tutorials/', views.GetAllTutorials),
	path('get_one_tutorial/', views.GetOneTutorial),
	path('get_all_faqs/', views.getFAQs),
	path('get_one_faq/', views.getFAQ)
]