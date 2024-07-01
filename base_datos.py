## Primero se deben instalar los siguientes librerias de python, ingresando el comando en la terminal de visual studio:
## Modulo para conectarse a base de datos mysql: pip install mysql.connector
## Modulo para enmascarar claves y proteger la informacion: pip install maskpass

## Primero se importan las librerias y modulos que se utilizaran
import mysql.connector, maskpass, hashlib

## Luego se importan las clases de modelo que se utilizaran con la Base de Datos
from modelo import Mecanico, Trabajo, Vehiculo, Cliente, Rol, Usuario #CORREGIR A LO QUE CORRESPONDE

## Se deben crear las clases CRUD de cada clase(trabajador, contactoemergencia, rol,etc.)
