from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_code = models.CharField(max_length=6)
    created_by = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.room_code
class Message(models.Model):
    value = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    rc = models.ForeignKey(Room,default=None,on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    def __str__(self):
        return self.value