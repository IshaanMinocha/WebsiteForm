from django.db import models
import os
# from .views import send_id_to_model

start_id = -1    
def unique_id_generator() :
    global start_id
    start_id+=1
    return (str((start_id+1)))

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    # filename = '%s.%s' % (str((start_id+2)), ext)
    filename = '%s.%s' % (unique_id_generator(), ext)
    return os.path.join('documents', filename)

# Create your models here.
class Document(models.Model):
    # docfile = models.FileField(upload_to='documents/')
    docfile = models.FileField(upload_to=content_file_name)
    name=models.CharField(max_length=40)
    unique_id=models.IntegerField(default=0)
    # start_id+=1
    def __str__(self):
        return self.name

