from django.contrib import admin
from django.urls import path
from .views import *

app_name = "MyMovie"
urlpatterns = [
    path("", Movie_Home, name = "home"),
    path("login_account", Login_Account, name = "login_account"),
    path("logout_account", Logout, name = "logout_account"),
    path("create_account/", Register, name = "register"),
    path("movie_booking_page/<int:st_id>/", SheetBookingPage, name = "sheet_booking"),
    #path("create_sheets/", Create_Sheets, name = "sheets"),
    path("contact", Movie_Contact, name = "contact"),
    path("payMentMake", MakePayment, name = "payment"),
    path("add_show_time", Admin_Add_ShowTime, name = "add_show_time"),
    path("all_movies", All_Movies, name = "all_movies"),
    path("add_movie_category", Admin_Add_Cat, name = "add_cat"),
    path("movie_details/<int:m_id>/", Movie_Details_Page, name = "movie_detail"),
    path("booking/<int:m_id>/", Movie_Confirmation, name = "confirmation"),
    path("PayCheck/<str:Usr>/", PayChack, name = "paycheck"),


    ]
