from django.contrib import admin
from . import models as db

admin.site.register(db.Room)
admin.site.register(db.Message)