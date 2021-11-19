from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    usuario_tipo = models.CharField(max_length=50)

class User(AbstractUser):
    tipousuario = models.ForeignKey(TipoUsuario,models.CASCADE)