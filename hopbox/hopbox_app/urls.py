"""hopbox_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

# need to add urlpatterns for different subscription boxes

urlpatterns = [
    path('', views.landing_page),
    path('home/', views.disp_home),
    path('register/', views.registration),
    path('register/create-user/', views.create_user),
    path('login/', views.login_page),
    path('login/login-user/', views.login),
    path('manage-account/', views.manage_account),
    path('update-account/', views.update_account),
    path('logout/', views.logout),
    path('cart/', views.disp_cart), 
    path('cart/order/', views.submit_order), 
    path('option/<int:optionNum>/', views.disp_option),
    path('option/review/', views.add_review),
    path('option/user_image/', views.add_user_image), 
]