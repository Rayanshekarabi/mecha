from django.db import models
from mongoengine import *

connect("mecha")


class User(DynamicDocument):
    pass


class Wallet(Document):
    pass


class Bullet(Document):
    pass


class profile(Document):
    pass
