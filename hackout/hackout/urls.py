from django.contrib import admin
from django.urls import path
from app1.views import SignupPage, LoginPage, HomePage, LogoutPage, generate_list, download_list_pdf, generate_packing_list_api, my_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', SignupPage, name='signup'),
    path('login/', LoginPage, name='login'),
    path('home/', HomePage, name='home'),
    path('logout/', LogoutPage, name='logout'),
    path('generate-list/', generate_list, name='generate_list'),
    path('download-list-pdf/', download_list_pdf, name='download_list_pdf'),
    path('generate/', generate_packing_list_api, name='generate_packing_list'),
    path('my_view/', my_view, name='my_view'),
]
