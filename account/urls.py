

from django.urls import path
from .views import (index,signup,logout_user,profile_image,activate_account,profile_account,
password_reset,
reset,
change_user,
two_factor)


app_name = "account"

urlpatterns = [
    path('', index,name="sign_in"),
    path('password_reset/',password_reset,name="password_reset"),
    path('signup/', signup,name="sign_up"),
    path('logout',logout_user,name="logout"),
    path('profile_image/',profile_image,name="upload_image"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate_account, name='activate'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        reset, name='reset'),
    path('account/',profile_account,name="profile"),
    path("change_user_password/",change_user,name="change_user"),
    path("two_factor/",two_factor,name="two_factor")
]



