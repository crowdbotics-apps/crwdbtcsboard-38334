from django.conf import settings
from django.db import models
from enum import Enum


class ApplicationType(Enum):
    WEB = "Web"
    MOBILE = "Mobile"

    @classmethod
    def choices(cls):
        return list(tuple((i.name, i.value) for i in cls))


class Application(models.Model):
    'Generated Model'

    DJANGO = 'Django'
    REACT = 'React'

    APP_FRAMEWORKS = [
        ("DJANGO", 'Django'),
        ("REACT", 'React'),
    ]

    WEB = "Web"
    MOBILE = "Mobile"

    APP_TYPES = [
        ("WEB", 'Web'),
        ("MOBILE", 'Mobile'),
    ]
    name = models.CharField(blank=False,max_length=50,)
    description = models.TextField(blank=False,max_length=20,)
    type = models.CharField(blank=False,choices=APP_TYPES,default="None",max_length=50,)
    framework = models.CharField(blank=False,choices=APP_FRAMEWORKS,default="None",max_length=50,)
    domain_name = models.CharField(blank=False,max_length=50,)
    def __str__(self):
        return f'{self.name} - {self.framework}'
