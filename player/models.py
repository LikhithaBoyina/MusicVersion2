from django.db import models
#Album Model


class Album(models.Model):
    Title = models.CharField(max_length=25)
    genere = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='upload/Albums/',null=True)
    created_At = models.DateTimeField(auto_now_add=True)
    Favourited_by = models.BooleanField(default=False)
    def __str__(self):
        return self.Title

#Song Model

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    Title=models.CharField(max_length=30)
    ANGER = 'Anger'
    SAD = 'Sad'
    FEAR = 'Fear'
    HAPPY = 'Happy'
    SURPRISE = 'Surprise' 
    NEUTRAL = 'Neutral'

    EMOTION_CHOICES = [
        (ANGER, 'Anger'),
        (SAD, 'Sad'),
        (FEAR, 'Fear'),
        (SURPRISE, 'Surprise'),
        (HAPPY, 'Happy'),
        (NEUTRAL, 'Neutral'),
    ]

    # Emotion field with choices
    Emotion = models.CharField(
        max_length=10,
        choices=EMOTION_CHOICES,
        default=NEUTRAL,  # You can set a default emotion if needed
    )
    File = models.FileField(upload_to ='uploads/Songs')


    def __str__(self):
        return self.Title


#Image Model
# myapp/models.py

class ImageData(models.Model):
    image = models.ImageField(upload_to='images/')