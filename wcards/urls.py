"""wcards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views

from gestionUsuarios.views import *
from gestionTarjetas.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',iniciar_sesion, name='login'),
    path('registrar_usuario/', registrar_usuario, name="registrarU"),
    path('editar_usuario/', editar_usuario, name="editarU"),
    path('mostrar_tarjeta/', mostrar_tarjeta, name="mostrarTarjeta"),
    path('registrar_tarjeta/',registrar_tarjeta,name="registrarT"),
    path('detalle_tarjeta/<str:id>',detalle_tarjeta,name="detalleT"),
    path('mis_listas/',mis_listas,name="listas"),
    path("baseWiki/", base_wiki,name='baseW'),
    path("logout/", cerrar_sesion, name='logout'),
    path("prueba/", prueba),
    path("password/", views.PasswordChangeView.as_view(), name='cambio_contraseña'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = error400

handler403 = error403

handler404 = error404

handler500 = error500



