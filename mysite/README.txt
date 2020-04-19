Pre requisitos:

En la carpeta mystie/ se ubica el archivo con los requisitos previos de intalación del sistema.
Para instalarlos se debe ejecutar el siguiente comado desde el shell ubicados en ./mysite:

pip install -r requirements.txt

Instalación:

Para poner en funcionamiento se deben correr dos servidores.

1- Desde la carpeta ./mysite/ ejecutar el comando python manage.py runserver
2- Desde la carpeta ./mysite/snipcartwagtaildemo/ ejecutar el comando python manage.py runserver 8080

Construido con:

Python
Django
Wagtail