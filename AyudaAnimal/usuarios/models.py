from django.contrib.auth.models import AbstractUser
from django.db import models


class diferentesUser(AbstractUser):
    MEDICO = 'MEDICO'
    RECEPCIONISTA = 'RECEPCIONISTA'
    ADMINISTRADOR = 'ADMINISTRADOR'
    OPCIONES_TIPO_USUARIO = [
        (MEDICO, 'Médico'),
        (RECEPCIONISTA, 'Recepcionista'),
        (ADMINISTRADOR, 'Administrador'),
    ]

    tipo_usuario = models.CharField(
        max_length=20,
        choices=OPCIONES_TIPO_USUARIO,
        default=RECEPCIONISTA,
    )

    grupos = models.ManyToManyField(
        'auth.Group',
        verbose_name='grupos',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario. Un usuario obtendrá todos los permisos concedidos a cada uno de sus grupos.',
        related_name="usuario_personalizado_grupos",
        related_query_name="usuario_personalizado",
    )

    permisos_usuario = models.ManyToManyField(
        'auth.Permission',
        verbose_name='permisos de usuario',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        related_name="usuario_personalizado_permisos",
        related_query_name="usuario_personalizado",
    )

class Medico(models.Model):
    usuario = models.OneToOneField('usuarios.diferentesUser', on_delete=models.CASCADE,)
    nombre = models.CharField(max_length=50)

    # Aquí puedes agregar más campos específicos para el perfil médico