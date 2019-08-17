from django.urls import path
from . import views

# Create urls here
"""

Create urls for each backend service, such as iam, catalog etc.
Example,
Home - Default home page related urls, (Web landing page) - path('', views.homepage, name='home')
IAM - Identity and access management servce. (Login, logout etc)
Upload image - 
Catalog -
"""


urlpatterns = [
    path('', views.homepage, name='home'),  # map home view

    #path('login_form/', views.login_form, name='login_form'),  # map user_login view
    path('login/', views.user_login, name='login'),  # map user_login view
    path('logout/', views.user_logout, name='logout'),  # map user_logout view
    path('signup/', views.user_signup, name='signup'),  # map user_signup view

    path('enquiry/', views.enquiry, name='enquiry'),  # map user_signup view

]