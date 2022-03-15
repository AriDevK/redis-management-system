# 🍱 Manejador BDD Redis
Interfaz grafica para realizar consultas basicas a una base de datos Redis, escrito en **Python** y usando **Tkinter**

![alt](https://github.com/Ari-Qu3sadillas/redis-management-system/blob/main/screenshots/app_esp.png)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Redis](https://img.shields.io/badge/redis-E05565?style=for-the-badge&logo=redis&logoColor=FFFFFF)
![Tkinter](https://img.shields.io/badge/Tkinter-FF9248?style=for-the-badge&logo=Ts&logoColor=FFFFFF)


<br><br>

## 📑 Tabla de Contenido
  - [Objetivo](#-objetivo)
  - [Dependencias-del-Proyecto](#-dependencias-del-proyecto)
  - [Estructura-de-Directorios](#-estructura-de-directorios)
  - [Instalacion](#-instalacion)
  - [Capturas de Pantalla](#-capturas-de-pantalla)

<br>


## 🎯 Objetivo
Realizar una interfaz grafica que permita la manipulacion de una base de datos Redis, esta interfaz debe de ser construida
con el lenguaje de programacion **Python** y la libreria **Tkinter**.

La interaccion con la base de datos se realizara mediante la libreria de **Redis** para el lenguaje Python y se deben de realizar
las funciones minimas de un CRUD como son Crear, Leer, Actualizar y Eliminar registros.

<br>

## 💡 Dependencias del Proyecto
El proyecto cuenta con las siguientes dependencias de terceros:
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Interfaces Graficas
- [Pillow](https://python-pillow.org)  - Manejo de Imagenes
- [Dotenv](https://github.com/theskumar/python-dotenv)  - Manejo de Variables de Entorno
- [Babel](https://babel.pocoo.org/en/latest/)   - Traducciones de texto


<br>

## 📂 Estructura de Directorios
```
redis-management
├─ requirements.txt     -> Archivo de dependencias del proyecto
└─ src                  -> Directorio del codigo fuente
   ├─ main.py           -> Punto de entrada de la aplicacion
   ├─ .env              -> Archivo de variables de entorno de la apliacion
   ├─ assets            -> Directorio de archivos multimedia del proyecto
   ├─ locale            -> Directorio con traducciones
   ├─ utils             -> Directorio con utilidades del proyecto (Redis e Idioma)
   └─ views             -> Directorio de vistas de la aplicacion
```
<br>

## ⚙ Instalacion
1. Clona el repositorio y dirigete al directorio.
```shell
$ git clone git@github.com:Ari-Qu3sadillas/redis-management-system.git
$ cd ./redis-management
```
2. Inicializa y Activa un entorno virtual
```shell
$ virtualenv venv
$ source venv/bin/activate   //Linux
> ./venv/script/activate.bat //Windows CMD
> ./venv/script/activate.ps1 //Windows PowerShell
```
3. Instala las dependencias:
```shell
$ pip install -r ./requirements.txt
```
4. Dirigete al directorio *src* y ejecuta el archivo *main.py*
```shell
$ cd src
$ python ./main.py
```
<br>

## 📷 Capturas de Pantalla
Menu de seleccion de idiomas <br>
![alt](https://github.com/Ari-Qu3sadillas/redis-management-system/blob/main/screenshots/menu_lang.png)
<br>
Interfaz grafica en Ingles <br>
![alt](https://github.com/Ari-Qu3sadillas/redis-management-system/blob/main/screenshots/app_en.png)
<br>
Interfaz grafica en Español <br>
![alt](https://github.com/Ari-Qu3sadillas/redis-management-system/blob/main/screenshots/app_esp.png)
<br>
Interfaz grafica en Noruego <br>
![alt](https://github.com/Ari-Qu3sadillas/redis-management-system/blob/main/screenshots/app_nor.png)
<br>
Proceso de Creacion <br>
![alt](https://github.com/Ari-Qu3sadillas/redis-management-system/blob/main/screenshots/create.PNG)
<br>
Proceso de Lectura <br>
![alt](https://github.com/Ari-Qu3sadillas/redis-management-system/blob/main/screenshots/read.PNG)
<br>
Proceso de Eliminar <br>
![alt](https://github.com/Ari-Qu3sadillas/redis-management-system/blob/main/screenshots/delete.PNG)

