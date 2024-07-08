# Se importa libreria hashlib para crear claves seguras
import hashlib

# Se crea funcion para crear clave que toma la clave ingresada por el usuario y la transforma en hash, 
# la que luego debe ser usada para agragarla a la BD
def crear_clave(clave):
    enc = clave.encode()
    hash = hashlib.md5(enc).hexdigest()
    return hash

# 01/07/2024
# Se crea clase trabajador con sus atributos y constructor
class Trabajador:
    def __init__(self, rut_trabajador, nombre_trabajador, apellido_trabajador, sexo, domicilio, telefono, cargo, fecha_ingreso, area, dpto, nombre_completo_emergencia, relacion, telefono_emergencia):
        self.__rut_trabajador = rut_trabajador
        self.__nombre_trabajador = nombre_trabajador
        self.__apellido_trabajador = apellido_trabajador
        self.__sexo = sexo
        self.__domicilio = domicilio
        self.__telefono = telefono
        self.__cargo = cargo
        self.__fecha_ingreso = fecha_ingreso
        self.__area = area
        self.__dpto = dpto
        self.__nombre_completo_emergencia = nombre_completo_emergencia
        self.__relacion = relacion
        self.__telefono_emergencia = telefono_emergencia

# Se crean funciones para obtener atributos:

    def obtener_rut_trabajador(self):
        return self.__rut_trabajador
    
    def obtener_nombre_trabajador(self):
        return self.__nombre_trabajador
    
    def obtener_apellido_trabajador(self):
        return self.__apellido_trabajador
    
    def obtener_sexo(self):
        return self.__sexo
    
    def obtener_domicilio(self):
        return self.__domicilio
    
    def obtener_telefono(self):
        return self.__telefono
    
    def obtener_cargo(self):
        return self.__cargo
    
    def obtener_fecha_ingreso(self):
        return self.__fecha_ingreso
    
    def obtener_area(self):
        return self.__area
    
    def obtener_dpto(self):
        return self.__dpto
    
    def obtener_nombre_completo_emergencia(self):
        return self.__nombre_completo_emergencia
    
    def obtener_relacion(self):
        return self.__relacion
    
    def obtener_telefono_emergencia(self):
        return self.__telefono_emergencia
    
    def obtener_nombre_completo_trabajador(self):
        return '{} {}'.format(self.obtener_nombre_trabajador(), self.obtener_apellido_trabajador())
    
# Se crean funciones para cambiar valores de atributos:
    
    def cambiar_rut_trabajador(self, rut_trabajador):
        self.__rut_trabajador = rut_trabajador

    def cambiar_nombre_trabajador(self, nombre_trabajador):
        self.__nombre_trabajador = nombre_trabajador

    def cambiar_apellido_trabajador(self, apellido_trabajador):
        self.__apellido_trabajador = apellido_trabajador

    def cambiar_sexo(self, sexo):
        self.__sexo = sexo

    def cambiar_domicilio(self, domicilio):
        self.__domicilio = domicilio

    def cambiar_telefono(self, telefono):
        self.__telefono = telefono

    def cambiar_rut_trabajador(self, rut_trabajador):
        self.__rut_trabajador = rut_trabajador

    def cambiar_cargo(self, cargo):
        self.__cargo = cargo

    def cambiar_fecha_ingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso

    def cambiar_area(self, area):
        self.__area = area

    def cambiar_dpto(self, dpto):
        self.__dpto = dpto

    def cambiar_nombre_completo_emergencia(self, nombre_completo_emergencia):
        self.__nombre_completo_emergencia = nombre_completo_emergencia

    def cambiar_relacion(self, relacion):
        self.__relacion = relacion

    def cambiar_telefono_emergencia(self, telefono_emergencia):
        self.__telefono_emergencia = telefono_emergencia

# 01/07/2024
# Se crea clase Carga_Familiar con sus atributos y constructor
class Carga_Familiar:
    def __init__(self, rut_carga, rut_trabajador, nombre_completo_carga, parentesco, sexo):
        self.__rut_carga = rut_carga
        self.__rut_trabajador = rut_trabajador
        self.__nombre_completo_carga = nombre_completo_carga
        self.__parentesco = parentesco
        self.__sexo = sexo

# Se crean funciones para obtener atributos:

    def obtener_rut_carga(self):
        return self.__rut_carga

    def obtener_rut_trabajador(self):
        return self.__rut_trabajador
    
    def obtener_nombre_completo_carga(self):
        return self.__nombre_completo_carga
    
    def obtener_parentesco(self):
        return self.__parentesco
    
    def obtener_sexo(self):
        return self.__sexo
    
# Se crean funciones para cambiar valores de atributos:
    
    def cambiar_rut_carga(self, rut_carga):
        self.__rut_carga = rut_carga

    def cambiar_rut_trabajador(self, rut_trabajador):
        self.__rut_trabajador = rut_trabajador

    def cambiar_nombre_completo_carga(self, nombre_completo_carga):
        self.__nombre_completo_carga = nombre_completo_carga

    def cambiar_parentesco(self, parentesco):
        self.__parentesco = parentesco
    
    def cambiar_sexo(self, sexo):
        self.__sexo = sexo

# 01/07/2024
# Se crea clase Rol con sus atributos y constructor
class Rol:
    def __init__(self, id_rol, nombre_rol):
        self.__id_rol = id_rol
        self.__nombre_rol = nombre_rol
        self.__descripcion = str()

# Se crean funciones para obtener atributos:

    def obtener_id_rol(self):
        return self.__id_rol

    def obtener_nombre_rol(self):
        return self.__nombre_rol
    
    def obtener_descripcion(self):
        return self.__descripcion
    
# Se crean funciones para cambiar valores de atributos:
    
    def cambiar_id_rol(self, id_rol):
        self.__id_rol = id_rol

    def cambiar_nombre_rol(self, nombre_rol):
        self.__nombre_rol = nombre_rol

    def cambiar_descripcion(self, descripcion):
        self.__descripcion = descripcion

# 01/07/2024
# Se crea clase Usuario con sus atributos y constructor
class Usuario:
    def __init__(self, nombre_usuario, clave, rol):
        self.__nombre_usuario = nombre_usuario
        self.__clave = clave
        self.__rol = rol
        self.__nombre = str()
        self.__apellido = str()
        self.__trabajador = None

# Se crean funciones para obtener atributos:

    def obtener_nombre_usuario(self):
        return self.__nombre_usuario

    def obtener_rol(self):
        return self.__rol
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_apellido(self):
        return self.__apellido
    
    def obtener_trabajador(self):
        return self.__trabajador
    
    def obtener_clave(self):
        return self.__clave
    
# Se crean funciones para cambiar valores de atributos:
    
    def cambiar_nombre_usuario(self, nombre_usuario):
        self.__nombre_usuario = nombre_usuario

    def cambiar_clave(self, clave):
        self.__clave = crear_clave(clave)

    def validar_clave(self, clave):
        hash = crear_clave(clave)
        return self.__clave == hash

    def cambiar_nombre(self, nombre):
        self.__nombre = nombre

    def cambiar_apellido(self, apellido):
        self.__apellido = apellido

    def cambiar_trabajador(self, trabajador):
        self.__trabajador = trabajador