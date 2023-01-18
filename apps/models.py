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
        (DJANGO, 'Django'),
        (REACT, 'React'),
    ]

    name = models.CharField("Name", max_length=50, blank=False)
    description = models.TextField("Description",
                                   blank=False, max_length=20)
    type = models.CharField("Description", max_length=50, choices=ApplicationType.choices(), blank=False, default=None)
    framework = models.CharField("Framework", max_length=50, choices=APP_FRAMEWORKS, blank=False,
                                 default=None)
    domain_name = models.CharField("Domain Name", max_length=50, blank=False)

    def __str__(self):
        return f"{self.name} - {self.framework}"
