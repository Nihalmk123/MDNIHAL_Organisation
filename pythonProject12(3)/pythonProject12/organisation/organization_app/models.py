import os
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
import os
from pathlib import Path
import time
# Create your models here.
from organisation import settings
from .common_lib import CommonLib


common_lib = CommonLib()

def society_file(instance, filename):

    try:
        if filename:
            name, ext = os.path.splitext(str(filename))
            # constituency = ClientConstituency.objects.get(client=instance.voter_basic_info.client)

            directory_path = settings.MEDIA_ROOT + common_lib.MEDIA_PATH_CHOICES['society']
            Path(directory_path).mkdir(parents=True, exist_ok=True)
            media_path = common_lib.MEDIA_PATH_CHOICES['society']
            updated_file_name = str(int(time.time())) + '_' + str(instance.id)
            return media_path + "%s%s" % (updated_file_name, ext)
    except Exception as e:
        print(str(e))


def office_file(instance, filename):

    try:
        if filename:
            name, ext = os.path.splitext(str(filename))
            # constituency = ClientConstituency.objects.get(client=instance.voter_basic_info.client)

            directory_path = settings.MEDIA_ROOT + common_lib.MEDIA_PATH_CHOICES['office']
            Path(directory_path).mkdir(parents=True, exist_ok=True)
            media_path = common_lib.MEDIA_PATH_CHOICES['office']
            updated_file_name = str(int(time.time())) + '_' + str(instance.id)
            return media_path + "%s%s" % (updated_file_name, ext)
    except Exception as e:
        print(str(e))


def institute_file(instance, filename):

    try:
        if filename:
            name, ext = os.path.splitext(str(filename))
            # constituency = ClientConstituency.objects.get(client=instance.voter_basic_info.client)

            directory_path = settings.MEDIA_ROOT + common_lib.MEDIA_PATH_CHOICES['institute']
            Path(directory_path).mkdir(parents=True, exist_ok=True)
            media_path = common_lib.MEDIA_PATH_CHOICES['institute']
            updated_file_name = str(int(time.time())) + '_' + str(instance.id)
            return media_path + "%s%s" % (updated_file_name, ext)
    except Exception as e:
        print(str(e))


class Designation(models.Model):
    name = models.CharField(max_length=120,unique=True)
    acronym = models.CharField(max_length=12)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Committee(models.Model):
    name=models.CharField(max_length=350,unique=True)
    acronym=models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Society(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(max_length=100,upload_to=society_file)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    www = models.URLField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False,default=datetime.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class OfficeBearerss(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(max_length=100,upload_to=office_file)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(default=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    committee=models.ForeignKey(Committee,on_delete=models.CASCADE)
    societyy=models.ForeignKey(Society,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Institute(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(max_length=100,upload_to=institute_file)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.IntegerField()
    www = models.URLField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(default=True)
    society=models.ForeignKey(Society,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    www = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(default=True)
    insitute=models.ForeignKey(Institute,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class ProgramCategoryy(models.Model):
    name = models.CharField(unique=True,max_length=100)
    acro_name = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Programm(models.Model):
    name = models.CharField(unique=True,max_length=100)
    program_category = models.ForeignKey(ProgramCategoryy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Streamm(models.Model):
    name = models.CharField(max_length=100)
    program_category = models.ForeignKey(ProgramCategoryy, on_delete=models.CASCADE)
    program = models.ForeignKey(Programm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class MainProgramm(models.Model):
    program_category = models.ForeignKey(ProgramCategoryy, on_delete=models.CASCADE)
    program = models.ForeignKey(Programm, on_delete=models.CASCADE)
    stream = models.ForeignKey(Streamm, on_delete=models.CASCADE)
    duration = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, default=datetime.now)
    status = models.BooleanField(default=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

