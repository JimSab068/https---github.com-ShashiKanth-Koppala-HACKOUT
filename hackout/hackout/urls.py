from django.contrib import admin
from django.urls import path
from app1.views import SignupPage, LoginPage, HomePage, LogoutPage,InputPage, download_list_pdf, generate_packing_list_api, list,LandingPage  # Removed generate_list and added list

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', LandingPage, name='landing'),
    path('signup/', SignupPage, name='signup'),
    path('login/', LoginPage, name='login'),
    path('home/', HomePage, name='home'),
    path('input/', InputPage, name='input'),
    path('list/', list, name='list'),   # New path for the list view
    path('download-list-pdf/', download_list_pdf, name='download_list_pdf'),
    path('generate_packing_list_api/', generate_packing_list_api, name='generate_packing_list_api'),
]
