from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator
from enum import Enum


class ApplicationType(Enum):
    WEB = "Web"
    MOBILE = "Mobile"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class ApplicationFramework(Enum):
    DJANGO = "Django"
    REACT = "React Native"

    @classmethod
    def choices(cls):
        return tuple((i.name, str(i.value)) for i in cls)


class Application(models.Model):
    'Generated Model'

    name = models.CharField("Name", max_length=50, blank=False)
    description = models.TextField("Description",
                                   blank=False, max_length=20)
    type = models.CharField("Description", max_length=50, choices=ApplicationType.choices(), blank=False, default=None)
    framework = models.CharField("Framework", max_length=50, choices=ApplicationFramework.choices(), blank=False, default=None)
    domain_name = models.CharField("Domain Name", max_length=50, blank=False)

    def __str__(self):
        return f"{self.name} - {self.framework}"
