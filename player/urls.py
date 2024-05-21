from django.urls import  path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    # # path('login',views.LoginView,name='login'),
    # # path('logout',views.LogoutView,name='logout'),
    # # path('register',views.registerView,name='register'),
    path('songs/<str:emotion>/', views.songs_by_emotion, name='songs_by_emotion'),
     path('search/', views.search, name='search'),
    path('AddFavourite/<int:pk>',views.AddFavourite,name='Fav'),
    path('predict_emotion/', views.predict_emotion, name='predict_emotion'),
    path('Album/<int:pk>',views.AlbumPage,name='album')
] 