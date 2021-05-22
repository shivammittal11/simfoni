from django.urls import path

from user.views import *

urlpatterns = [
    path('signup/', user_signup),
    path('search_supplier/', search_supplier),
]
