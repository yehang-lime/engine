from django.db import models


# Create your models here.
class Hello:
    message = ''

    def __init__(self, message):
        self.message = message
