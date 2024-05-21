from django.shortcuts import render,redirect,reverse
from .forms import *
from django.core import serializers
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import tensorflow as tf
import numpy as np
# from PIL import Image
from tensorflow.keras.models import load_model
import cv2
import base64
import json
import os


info = {}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
haarcascade_path = os.path.join(BASE_DIR, 'haarcascade_frontalface_default.xml')
cascade = cv2.CascadeClassifier(haarcascade_path)
label_map = ['Anger', 'Neutral', 'Fear', 'Happy', 'Sad', 'Surprise']


model_path = os.path.join(BASE_DIR, 'model.h5')
model = load_model(model_path)



def index(request):
        albums = Album.objects.all()
        return render(request,'player/index.html',{'Albums':albums})

def songs_by_emotion(request,emotion):
    # Validate if the provided emotion is one of the choices
    if emotion not in dict(Song.EMOTION_CHOICES).keys():
        # return render(request, 'error.html', {'error_message': 'Invalid emotion'})
        pass

    # Retrieve songs with the specified emotion
    songs = Song.objects.filter(Emotion=emotion)
    print("Lokesh")

    # You can pass the 'songs' queryset to your template
    return render(request, 'player/songs.html', {'emotion': emotion, 'songs': songs})


@csrf_exempt
@require_POST
def predict_emotion(request):
    if request.body:
        json_data = json.loads(request.body.decode('utf-8'))
        data_url = json_data.get('image_data')
        
        if data_url:
            _, encoded = data_url.split(",", 1)
            image_data = np.frombuffer(base64.b64decode(encoded), dtype=np.uint8)
            frame = cv2.imdecode(image_data, 1)
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = cascade.detectMultiScale(gray, 1.4, 1)

            for x, y, w, h in faces:
                roi = gray[y:y+h, x:x+w]
                roi = cv2.resize(roi, (48, 48))
                roi = roi / 255.0
                roi = np.reshape(roi, (1, 48, 48, 1))

                prediction = model.predict(roi)
                prediction = np.argmax(prediction)
                prediction = label_map[prediction]
                print(type(prediction))

                return JsonResponse({'emotion': prediction})
    
    return JsonResponse({'error': 'No face detected'})





# def LoginView(request):
#     url = True
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         try:
#             email = User.objects.get(email=email.lower()).username
#             user = authenticate(username=email,password=password)
#             if user is not None:
#                  login(request,user)
#                  return redirect('home')
#             else:
#                  messages.error('user not found !')
#                  return redirect('login')
#         except:
#                 messages.error(request,'User Not Found')
#                 return redirect('login')
#     return render(request,'player/login.html',{'url':url})

# def registerView(request):
#     url = True
#     newuser = CreateUserForm()
#     if request.method == 'POST':
#          print('inform')
#          newuser = CreateUserForm(request.POST)
#          print(newuser)
#          if newuser.is_valid():
#               newuser.save()
#               messages.success(request,'Registration Sucessfull !')
#               return redirect('login')
#     return render(request,'player/register.html',{'url':url,'form':newuser})

# def LogoutView(request):
#      logout(request)
#      return redirect('login')


def AddFavourite(request,pk):
    album = Album.objects.get(id=pk)
    albums = Album.objects.all()
    album.Favourited_by = not album.Favourited_by
    album.save()
    return render(request,'player/index.html',{'Albums':albums})
    
def AlbumPage(request,pk):
     songs = Song.objects.filter(album = Album.objects.get(id=pk))
     album = Album.objects.get(id=pk)
     return render(request,'player/Album.html',{'songs':songs,'album':album})   


def search(request):
    query = request.GET.get('q')

    if query:
        # Search for albums and songs with partial title match
        albums = Album.objects.filter(Title__icontains=query)
        songs = Song.objects.filter(Title__icontains=query)
    else:
        albums = Song.objects.none()
        songs = Song.objects.none()

    return render(request, 'player/search_results.html', {'albums': albums, 'songs': songs, 'query': query})


          
