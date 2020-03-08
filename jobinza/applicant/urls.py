#from django.urls import path 
#from . import views

#urlpatterns = [
#    path('', views.home, name='home'),
#]

from django.urls import path
from . import views

app_name = 'applicant'

urlpatterns = [
#	path('details/', views.job_details, name="job_details"),
	path('details/<int:job_id>/', views.job_details, name='emp_detail'),
	path('profile/<str:user_name>/', views.profile_info, name='profile'),
	path('addinfo/',views.addinfo, name='addinfo'),
	#path('details/', views.job_details, name='emp_detail'),

]