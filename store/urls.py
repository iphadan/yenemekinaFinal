from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('post/',views.post,name='post'),
    path('detail/<int:id>/',views.carDetail,name='detail'),
    path('sold/<int:id>/',views.sold,name='sold'),
    path('editPost/<int:id>/',views.editPost,name='editPost'),
    path('soldCars/',views.soldCars,name='solcCars'),
    path('seedSuperUser/<str:username>/<str:password>',views.seedSuperUser,name='seedSuperUser'),

]