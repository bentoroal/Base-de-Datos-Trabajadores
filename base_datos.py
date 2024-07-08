## Primero se deben instalar los siguientes librerias de python, ingresando el comando en la terminal de visual studio:
## Modulo para conectarse a base de datos mysql: pip install mysql.connector
## Modulo para enmascarar claves y proteger la informacion: pip install maskpass

## Primero se importan las librerias y modulos que se utilizaran
import mysql.connector, maskpass, hashlib

## Luego se importan las clases de modelo que se utilizaran con la Base de Datos
from modelo import Trabajador, Carga_Familiar, Rol, Usuario

## CRUDS de clases, creados 4/7/2024
#Crud de Trabajador
class CrudTrabajador:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'programa_trabajadores_db')
    #Esta funcion obtiene una lista de todos los trabajadores registrados
    def obtener(self):
        trabajadores = []
        cursor = self.conexion.cursor()
        sql = 'select * from trabajador'
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            nuevo = Trabajador(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7], row[8], row[9], row[10], row[11], row[12])
            trabajadores.append(nuevo)
        return trabajadores
    #VER SI HAY CONFLICTOS AL HABER CAMPOS NO OBLIGATORIOS PERO QUE IGUAL SE HAN INCLUIDO EN LOS CONSTRUCTORES
    def crear(self, trabajador):
        cursor = self.conexion.cursor()
        sql = 'INSERT INTO trabajador VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        vals = (trabajador.obtener_rut_trabajador(), trabajador.obtener_nombre_trabajador(), trabajador.obtener_apellido_trabajador(), 
                trabajador.obtener_sexo(), trabajador.obtener_domicilio(), trabajador.obtener_telefono(), trabajador.obtener_cargo(),
                trabajador.obtener_fecha_ingreso(), trabajador.obtener_area(), trabajador.obtener_dpto(), trabajador.obtener_nombre_completo_emergencia(),
                trabajador.obtener_relacion(), trabajador.obtener_telefono_emergencia())
        cursor.execute(sql, vals)
        self.conexion.commit()

    def buscar(self, rut):
        cursor = self.conexion.cursor()
        sql = 'SELECT * from trabajador WHERE rut_trabajador = %s'
        vals = (rut,)
        cursor.execute(sql, vals)
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            return Trabajador(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        
    def eliminar(self, rut):
        cursor = self.conexion.cursor()
        sql = 'DELETE FROM trabajador WHERE rut_trabajador = %s'
        vals = (rut,)
        cursor.execute(sql, vals)
        self.conexion.commit()

    def modificar(self, trabajador):
        cursor = self.conexion.cursor()
        sql = 'UPDATE trabajador SET  nombre_trabajador = %s, apellido_trabajador = %s, sexo = %s, domicilio = %s, telefono = %s, cargo = %s, fecha_ingreso = %s, area = %s, dpto = %s, nombre_completo_emergencia = %s, relacion = %s, telefono_emergencia = %s WHERE rut_trabajador = %s'
        vals = (trabajador.obtener_nombre_trabajador(), trabajador.obtener_apellido_trabajador(), 
                trabajador.obtener_sexo(), trabajador.obtener_domicilio(), trabajador.obtener_telefono(), trabajador.obtener_cargo(),
                trabajador.obtener_fecha_ingreso(), trabajador.obtener_area(), trabajador.obtener_dpto(), trabajador.obtener_nombre_completo_emergencia(),
                trabajador.obtener_relacion(), trabajador.obtener_telefono_emergencia(), trabajador.obtener_rut_trabajador())
        cursor.execute(sql, vals)
        self.conexion.commit()

#Crud de Carga Familiar de trabajador
class CrudCargaFamiliar:

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'programa_trabajadores_db'
        )

    def crear(self, carga):
        cursor = self.conexion.cursor()
        sql = 'INSERT INTO cargas_familiares VALUES(%s, %s, %s, %s, %s)'
        vals = (carga.obtener_rut_carga(), carga.obtener_rut_trabajador(),
                carga.obtener_nombre_completo_carga(), carga.obtener_parentesco(), carga.obtener_sexo())
        cursor.execute(sql, vals)
        self.conexion.commit()

    def obtener(self):
        cargas = []
        cursor = self.conexion.cursor()
        sql = 'select * from cargas_familiares'
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            nuevo = Carga_Familiar(row[0], row[1], row[2], row[3], row[4])
            cargas.append(nuevo)
        return cargas
    
    def buscar(self, rut_carga):
        cursor = self.conexion.cursor()
        sql = 'SELECT * from cargas_familiares WHERE rut_carga = %s'
        vals = (rut_carga,)
        cursor.execute(sql, vals)
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            return Carga_Familiar(row[0], row[1], row[2], row[3], row[4])
        
    def eliminar(self, rut_carga):
        cursor = self.conexion.cursor()
        sql = 'DELETE FROM cargas_familiares WHERE rut_carga = %s'
        vals = (rut_carga,)
        cursor.execute(sql, vals)
        self.conexion.commit()

#Crud Usuario
class CrudUsuario:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'programa_trabajadores_db')
    
    def buscar_usuario(self, nombre_usuario):
        try:
            cursor = self.conexion.cursor()
            sql = 'select * from usuario join rol on usuario.id_rol = rol.id_rol where nombre_usuario=%s'
            val = (nombre_usuario,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result is not None:
                rol = Rol(id_rol=result[6], nombre_rol=result[7])
                rol.cambiar_descripcion(result[8])
                usuario = Usuario(nombre_usuario=result[0], clave=result[1], rol=rol)
                usuario.cambiar_nombre(result[2])
                usuario.cambiar_apellido(result[3])
                if result[5] is not None:
                    crud_usu = CrudTrabajador()
                    tra = crud_usu.buscar(result[5])
                    usuario.cambiar_trabajador(tra)
                return usuario
            else:
                return None
        except mysql.connector.Error as err:
            raise Exception('Error de base de datos: {}'.format(err))

    def crear_usuario(self, usuario:Usuario, clave:str):
        try:
            hash = hashlib.md5(clave.encode()).hexdigest()
            cursor = self.conexion.cursor()
            sql = 'insert into usuario values (%s, %s, %s, %s, %s, %s)'
            val = (
                usuario.obtener_nombre_usuario(),
                hash,
                usuario.obtener_nombre(),
                usuario.obtener_apellido(),
                usuario.obtener_rol().obtener_id_rol(),
                usuario.obtener_trabajador()
            )
            cursor.execute(sql, val)
            self.conexion.commit()
        except mysql.connector.Error as err:
            raise Exception('Error de base de datos: {}'.format(err))

    def obtener_usuarios(self):
        try:
            usuarios = []
            cursor = self.conexion.cursor()
            sql = 'select * from usuario'
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                usuario = self.buscar_usuario(row[0])
                usuarios.append(usuario)
            return usuarios
        except mysql.connector.Error as err:
            raise Exception('Error de base de datos: {}'.format(err))
        
    def eliminar(self, nom_usu):
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM usuario WHERE nombre_usuario = '{}'".format(nom_usu)
            cursor.execute(sql)
            self.conexion.commit()
        except mysql.connector.Error as err:
            raise Exception('Error de base de datos: {}'.format(err))
    
    def cambiar_clave(self, nom_usu, hash):
        try:
            cursor = self.conexion.cursor()
            sql = 'UPDATE usuario SET hash_clave = %s WHERE nombre_usuario = %s '
            val = (hash, nom_usu)
            cursor.execute(sql, val)
            self.conexion.commit()
        except mysql.connector.Error as err:
            raise Exception('Error de base de datos: {}'.format(err))
