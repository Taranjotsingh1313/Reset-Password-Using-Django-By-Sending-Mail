from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('index/',views.main,name="main"),
    path('changepass/<str:id>/',views.changepassword,name="changepassword"),
    path('forgetpassword/',views.fpass,name='fpass')
]
 