# Proyecto Django para la renderización de usuarios

## Instalación de Django y Django REST Framework

_Comandos para la instalación de Django y Django REST Framework_

```
python -m pip install django
python -m pip install djangorestframework
python -m pip install django-cors-headers
```

## Conexión de Django con Oracle XE

_Comandos para la conexión con base de datos Oracle_

```
pip install cx_oracle
```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'localhost:1521/XEPDB1',
        'USER': 'USER_NAME',
        'PASSWORD': 'USER_PASSWORD',
    }
}
```

## Creación de Proyecto

_Comandos para creación de proyecto en Django_

```
django-admin startproject nombre_proyecto .
python manage.py startapp core
python manage.py migrate
```
_Comandos para creación de usuario administrador de la base de datos en Django_

```
python manage.py createsuperuser --email admin@correo.cl --username nombre_usuario
```

