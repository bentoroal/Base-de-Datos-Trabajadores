from modelo import Trabajador, Usuario, Carga_Familiar, Rol 
from base_datos import CrudTrabajador, CrudUsuario, CrudCargaFamiliar
import mysql.connector, hashlib, maskpass

#Clase menú creada 06/07/2024
#Clase menú se utiliza para ejecutar diversas funciones necesarias para la ejecucion del programa.
class Menu:
    def conectar_bd(self):
        self.conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'programa_trabajadores_db')


##FUNCIONES DE TRABAJADORES:

    #Funcion lista trabajadores de forma simple, recibe como argumento una lista de los trabajadores      
    def listar_trabajadores(self, trabajadores):
        print('')
        print('Trabajadores registrados:')
        for tra in trabajadores:
            print('----------------------------------------------------------------------')
            print('Rut: ', tra.obtener_rut_trabajador())
            print('Nombre Completo: ', tra.obtener_nombre_completo_trabajador())
            print('Sexo: ',tra.obtener_sexo())
            print('Cargo: ',tra.obtener_cargo())


    #Funcion lista trabajadores que coincidan con los filtros seleccionados por el usuario, recibe como argumento una lista de los trabajadores 
    # Y los campos para filtrar seleccionados por el usuario
    def listar_trabajadores_filtro(self, trabajadores, sexo, cargo, area):
        print('')
        print('Trabajadores registrados filtrados por sexo, area y/o cargo: ')
        for tra in trabajadores:
            cont= 0
            if tra.obtener_sexo()==sexo and tra.obtener_cargo()==cargo and tra.obtener_area()==area:
                print('----------------------------------------------------------------------')
                print('Rut: ', tra.obtener_rut_trabajador())
                print('Nombre Completo: ', tra.obtener_nombre_completo_trabajador())
                print('Sexo: ',tra.obtener_sexo())
                print('Domicilio: ',tra.obtener_domicilio())
                print('Telefono: ',tra.obtener_telefono())
                print('Cargo: ',tra.obtener_cargo())
                print('Fecha de ingreso: ',tra.obtener_fecha_ingreso())
                print('Area: ',tra.obtener_area())
                print('Dpto: ',tra.obtener_dpto())
                print('Nombre de contacto de emergencia: ',tra.obtener_nombre_completo_emergencia())
                print('Relacion: ',tra.obtener_relacion())
                print('Telefono de emergencia: ',tra.obtener_telefono_emergencia())
        if cont == 0:
                print('No se han encontrado trabajadores que cumplan los filtros establecidos')

    #Funcion muestra los datos del trabajador que ha ingresado al sistema
    def listar_propio_trabajador(self, trabajadores, rut):
        print('')
        print('Datos del trabajador: ')
        for tra in trabajadores:
            if tra.obtener_rut_trabajador()==rut:
                print('----------------------------------------------------------------------')
                print('Rut: ', tra.obtener_rut_trabajador())
                print('Nombre Completo: ', tra.obtener_nombre_completo_trabajador())
                print('Sexo: ',tra.obtener_sexo())
                print('Domicilio: ',tra.obtener_domicilio())
                print('Telefono: ',tra.obtener_telefono())
                print('Cargo: ',tra.obtener_cargo())
                print('Fecha de ingreso: ',tra.obtener_fecha_ingreso())
                print('Area: ',tra.obtener_area())
                print('Dpto: ',tra.obtener_dpto())
                print('Nombre de contacto de emergencia: ',tra.obtener_nombre_completo_emergencia())
                print('Relacion: ',tra.obtener_relacion())
                print('Telefono de emergencia: ',tra.obtener_telefono_emergencia())

    #Funcion permite agregar carga familiar asociada al rut del trabajador que ingresa
    def crear_carga(self,crud_carga, rut_trabajador):
        print('')
        while True:
            print('----------------------------------------------------------------------')
            print('Ingresar nueva Carga Familiar')      
            rut = input('Ingrese el rut de la carga familiar a ingresar sin puntos: ')
            carga = crud_carga.buscar(rut)
            if carga == None:
                nombre = input('Ingrese el nombre completo de la carga familiar: ')
                parentesco = input('Ingrese el parentesco de la carga familiar con el trabajador: ')
                sexo = input('Ingrese el sexo de la carga, h para hombre o m para mujer: ')
                carg = Carga_Familiar(rut, rut_trabajador, nombre, parentesco, sexo)
                crud_carga.crear(carg)
                print('Carga Familiar registrada exitosamente')
                break
            else:
                print('El rut de la carga ingresado ya se encuentra registrado, intente nuevamente')

    #Funcion permite listar las cargas asociadas al rut del trabajador que ingresa
    def listar_cargas(self, cargas, rut):
        print('')
        print('Cargas Familiares registradas:')
        for car in cargas:
            if car.obtener_rut_trabajador()==rut:
                print('----------------------------------------------------------------------')
                print('Rut de la carga familiar: ', car.obtener_rut_carga())
                print('Nombre Completo: ', car.obtener_nombre_completo_carga())
                print('Parentesco: ', car.obtener_parentesco())
                print('Sexo: ', car.obtener_sexo())
               
    #Funcion permite mostrar al usuario sus datos personales actualez, antes de modificarlos
    def listar_datos_personales(self, trabajadores, rut,):
        print('')
        for tra in trabajadores:
            if tra.obtener_rut_trabajador()==rut:
                print('----------------------------------------------------------------------')
                print('Rut: ', tra.obtener_rut_trabajador())
                print('Nombre Completo: ', tra.obtener_nombre_completo_trabajador())
                print('Sexo: ',tra.obtener_sexo())
                print('Domicilio: ',tra.obtener_domicilio())
                print('Telefono: ',tra.obtener_telefono())

    #Funcion permite modificar datos personales del usuario
    def cambiar_datos_personales(self, crud_tra, rut):
        print('')
        print('Modificar datos personales del trabajador')
        print('Ingrese los nuevos datos personales a continuacion: ')
        tra = crud_tra.buscar(rut)
        nombre_trabajador = input('Ingrese el nuevo nombre del trabajador: ')
        apellido_trabajador = input('Ingrese el nuevo apellido del trabajador: ')
        sexo = input("Ingrese el sexo del trabajador, h para hombre y m para mujer: ").lower()
        while not(sexo== 'h' or  sexo== 'm'):
            print('sexo no valido, recuerde que solo puede ser h para hombre o m para mujer. Intente otra vez')
            sexo = input("Ingrese el sexo del trabajador, h para hombre y m para mujer: ").lower()
        domicilio = input("Ingrese el domicilio del trabajador con el formato calle numero, comuna, region: ")
        while True:
            try:
                telefono = int(input("Ingresa tu número de teléfono: "))
                break 
            except ValueError:
                print("Error: Recuerda que solo puedes ingresar numeros.")
        tra.cambiar_nombre_trabajador(nombre_trabajador)
        tra.cambiar_apellido_trabajador(apellido_trabajador)
        tra.cambiar_sexo(sexo)
        tra.cambiar_domicilio(domicilio)
        tra.cambiar_telefono(telefono)
        crud_tra.modificar(tra)
        print('')
        print('Datos personales modificados correctamente') 

    #Funcion muestra al usuario sus datos de emergencia asociados
    def listar_datos_emergencia(self, trabajadores, rut,):
        print('')
        for tra in trabajadores:
            if tra.obtener_rut_trabajador()==rut:
                print('----------------------------------------------------------------------')
                print('Rut de trabajador: ', tra.obtener_rut_trabajador())
                print('Nombre de contacto de emergencia: ', tra.obtener_nombre_completo_emergencia())
                print('Relacion: ',tra.obtener_relacion())
                print('Telefono de contacto de emergencia: ',tra.obtener_telefono_emergencia())

    #Funcion permite modificar datos de emergencia al usuario
    def cambiar_datos_emergencia(self, crud_tra, rut):
        print('')
        print('Modificar datos de emergencia del trabajador')
        print('Ingrese los nuevos datos de emergencia a continuacion: ')
        tra = crud_tra.buscar(rut)
        nombre_emergencia = input('Ingrese el nuevo nombre del contacto de emergencia: ')
        relacion = input('Ingrese la relacion del contacto de emergencia con el trabajador: ')
        while True:
            try:
                telefono_emergencia = int(input("Ingresa el número de teléfono de emergencia: "))
                break 
            except ValueError:
                print("Error: Recuerda que solo puedes ingresar numeros.")
        tra.cambiar_nombre_completo_emergencia(nombre_emergencia)
        tra.cambiar_relacion(relacion)
        tra.cambiar_telefono_emergencia(telefono_emergencia)
        crud_tra.modificar(tra)
        print('')
        print('Datos de emergencia modificados correctamente') 
    


## Funciones relacionadas al USUARIO:

    #Funcion permite mostrar los usuarios registrados    
    def listar_usuarios(self,usuarios):
        print('Usuarios registrados:')
        for usu in usuarios:
            print('----------------------------------------------------------------------')
            print('Nombre de usuario: ', usu.obtener_nombre_usuario())
            print('Rol: ', usu.obtener_rol().obtener_nombre_rol())
            print('Nombre: ',usu.obtener_nombre())
            print('Apellido: ',usu.obtener_apellido())

    def ejecutar(self):
            self.imprimir_menu()

crud_tra= CrudTrabajador()
crud_usu= CrudUsuario()
crud_car= CrudCargaFamiliar()

while True:
    menu = Menu()
    print('Bienvenido al sistema de Base de Datos de Trabajadores')
    print('Inicio de sesión')
    nombre = input('Ingrese el nombre de usuario: ')
    #maskpass esconde clave ingresada por usuario
    clave = maskpass.askpass('Ingrese la clave: ')
    #Se busca el usuario en abse de datos con el nombre de usuario a ver si existe o no
    usuario = crud_usu.buscar_usuario(nombre)
    if usuario is None:
        print('Error: el usuario no existe!')
    else:
        if usuario.validar_clave(clave):
            rol = usuario.obtener_rol().obtener_nombre_rol()
            print('Bienvenido {} {} ({})!'.format(
                usuario.obtener_nombre(),
                usuario.obtener_apellido(),
                rol
                ))
        
            if rol == 'funcionario_rrhh':
                while True:
                    print( """
                    1) Ingresar nuevo trabajador
                    2) Listado simple de trabajadores
                    3) Cerrar Sesión
                    """)
                    opcion = input("Elija una opción: ")
                    if opcion == '1':
                        print('Ingresar nuevo trabajador')
                        opc = 'si'
                        while opc == 'si':
                            print('Datos Personales')
                            rut_trabajador = input('Ingrese el rut sin puntos del trabajador a ingresar: ')
                            tra = crud_tra.buscar(rut_trabajador)
                            if tra == None:
                                nombre_trabajador = input('Ingrese el nombre del trabajador: ')
                                apellido_trabajador = input('Ingrese el apellido del trabajador: ')
                                sexo = input("Ingrese el sexo del trabajador, h para hombre y m para mujer: ").lower()
                                while not(sexo== 'h' or  sexo== 'm'):
                                    print('sexo no valido, recuerde que solo puede ser h para hombre o m para mujer. Intente otra vez')
                                    sexo = input("Ingrese el sexo del trabajador, h para hombre y m para mujer: ").lower()
                                domicilio = input("Ingrese el domicilio del trabajador con el formato calle numero, comuna, region: ")
                                while True:
                                    try:
                                        telefono = int(input("Ingresa tu número de teléfono: "))
                                        break 
                                    except ValueError:
                                        print("Error: Recuerda que solo puedes ingresar numeros.")
                                print('Datos Laborales')
                                cargo = input("Ingrese el cargo del trabajador, estos pueden ser Asistente, Conductor, Administrativo, Jefe De RRHH, Bodeguero o Ejecutivo: ").title()
                                while not(cargo == 'Asistente' or  cargo == 'Conductor' or cargo == 'Administrativo' or cargo == 'Jefe De RRHH' or cargo == 'Bodeguero' or cargo == 'Ejecutivo'):
                                    print('cargo no valido, intente otra vez')
                                    cargo = input("Ingrese el cargo del trabajador, estos pueden ser Asistente, Conductor, Administrativo, Jefe De RRHH, Bodeguero o Ejecutivo: ").title()
                                fecha_ingreso = input("Ingrese la fecha de ingreso del trabajador con el formato AAAA-MM-DD: ")
                                area = input("Ingrese el area del trabajador, puede ser Soporte, Transporte, Ventas, Marketing, Remuneraciones o Jefatura: ").title()
                                while not(area == 'Soporte' or area == 'Transporte' or area == 'Ventas' or area == 'Marketing' or area == 'Remuneraciones' or area == 'Jefatura'):
                                    print('area no valida, recuerde que solo puede ser h para hombre o m para mujer. Intente otra vez')
                                    area = input("Ingrese el area del trabajador, puede ser Soporte, Transporte, Ventas, Marketing, Remuneraciones o Jefatura: ").title()
                                dpto = input('Ingrese el dpto del trabajador: ')
                                print('Contacto de Emergencia')
                                nombre_completo_emergencia = input('Ingrese el nombre completo del contacto de emergencia: ')
                                relacion =input('Ingrese la relacion del contacto de emergencia con el trabajador: ')
                                while True:
                                    try:
                                        telefono_emergencia = int(input('Ingrese el telefono de emergencia del contacto de emergencia: '))
                                        break 
                                    except ValueError:
                                        print("Error: Recuerda que solo puedes ingresar numeros.")
                                nuevo= Trabajador(rut_trabajador, nombre_trabajador, apellido_trabajador, sexo, domicilio, telefono, cargo, fecha_ingreso,area, dpto, nombre_completo_emergencia,relacion,telefono_emergencia)
                                crud_tra.crear(nuevo)
                                print('Trabajador {} {} rut: {} agregado correctamente'.format(nombre_trabajador, apellido_trabajador, rut_trabajador))

                                opc = input('Desea agregar otro usuario? Si o No: ').lower() 
                                if not(opc== 'si' or opc =='no'):
                                    print('Respuesta no valida, vuelva a intentarlo')
                                    opc = input('Desea agregar otro usuario? Si o No: ').lower()
                                if opc == 'no':
                                    break
                            
                            else:
                                print('El rut ingresado ya se encuentra registrado, intente nuevamente')
                    if opcion == '2':
                        menu.listar_trabajadores(crud_tra.obtener())
                    if opcion == '3':
                        break
                    if not(opcion == '1' or opcion =='2' or opcion == '3'):
                        print("No ha seleccionado una opcion valida, vuelva a intentarlo")

            if rol == 'jefe_rrhh':
                while True:
                    print("""
                    1) Ingresar nuevo trabajador
                    2) Listado simple de trabajadores
                    3) Listado con filtros de trabajadores
                    4) Cerrar Sesión
                    """)
                    opcion = input("Elija una opción: ")
                    if opcion == '1':
                        print('Ingresar nuevo trabajador')
                        opc = 'si'
                        while opc == 'si':
                            print('Datos Personales')
                            rut_trabajador = input('Ingrese el rut sin puntos del trabajador a ingresar: ')
                            tra = crud_tra.buscar(rut_trabajador)
                            if tra == None:
                                nombre_trabajador = input('Ingrese el nombre del trabajador: ')
                                apellido_trabajador = input('Ingrese el apellido del trabajador: ')
                                sexo = input("Ingrese el sexo del trabajador, h para hombre y m para mujer: ").lower()
                                while not(sexo== 'h' or  sexo== 'm'):
                                    print('sexo no valido, recuerde que solo puede ser h para hombre o m para mujer. Intente otra vez')
                                    sexo = input("Ingrese el sexo del trabajador, h para hombre y m para mujer: ").lower()
                                domicilio = input("Ingrese el domicilio del trabajador con el formato calle numero, comuna, region: ")
                                while True:
                                    try:
                                        telefono = int(input("Ingresa tu número de teléfono: "))
                                        break 
                                    except ValueError:
                                        print("Error: Recuerda que solo puedes ingresar numeros.")
                                print('Datos Laborales')
                                cargo = input("Ingrese el cargo del trabajador, estos pueden ser Asistente, Conductor, Administrativo, Jefe De RRHH, Bodeguero o Ejecutivo: ").title()
                                while not(cargo == 'Asistente' or  cargo == 'Conductor' or cargo == 'Administrativo' or cargo == 'Jefe De RRHH' or cargo == 'Bodeguero' or cargo == 'Ejecutivo'):
                                    print('cargo no valido, intente otra vez')
                                    cargo = input("Ingrese el cargo del trabajador, estos pueden ser Asistente, Conductor, Administrativo, Jefe De RRHH, Bodeguero o Ejecutivo: ").title()
                                fecha_ingreso = input("Ingrese la fecha de ingreso del trabajador con el formato AAAA-MM-DD: ")
                                area = input("Ingrese el area del trabajador, puede ser Soporte, Transporte, Ventas, Marketing, Remuneraciones o Jefatura: ").title()
                                while not(area == 'Soporte' or area == 'Transporte' or area == 'Ventas' or area == 'Marketing' or area == 'Remuneraciones' or area == 'Jefatura'):
                                    print('area no valida, recuerde que solo puede ser h para hombre o m para mujer. Intente otra vez')
                                    area = input("Ingrese el area del trabajador, puede ser Soporte, Transporte, Ventas, Marketing, Remuneraciones o Jefatura: ").title()
                                dpto = input('Ingrese el dpto del trabajador: ')
                                print('Contacto de Emergencia')
                                nombre_completo_emergencia = input('Ingrese el nombre completo del contacto de emergencia: ')
                                relacion =input('Ingrese la relacion del contacto de emergencia con el trabajador: ')
                                while True:
                                    try:
                                        telefono_emergencia = int(input('Ingrese el telefono de emergencia del contacto de emergencia: '))
                                        break 
                                    except ValueError:
                                        print("Error: Recuerda que solo puedes ingresar numeros.")
                                nuevo= Trabajador(rut_trabajador, nombre_trabajador, apellido_trabajador, sexo, domicilio, telefono, cargo, fecha_ingreso,area, dpto, nombre_completo_emergencia,relacion,telefono_emergencia)
                                crud_tra.crear(nuevo)
                                print('Trabajador {} {} rut: {} agregado correctamente'.format(nombre_trabajador, apellido_trabajador, rut_trabajador))

                                opc = input('Desea agregar otro usuario? Si o No: ').lower() 
                                if not(opc== 'si' or opc =='no'):
                                    print('Respuesta no valida, vuelva a intentarlo')
                                    opc = input('Desea agregar otro usuario? Si o No: ').lower()
                                if opc == 'no':
                                    break
                            
                            else:
                                print('El rut ingresado ya se encuentra registrado, intente nuevamente')
                    if opcion == '2':
                        menu.listar_trabajadores(crud_tra.obtener())
                    if opcion =='3':
                        print('A continuacion puede seleccionar que filtros desea aplicar al listado de trabajadores')
                        #En esta parte del codigo se pide al usuario que seleccione los filtros para luego mandarlos como argumentos a la funcion de listar con filtrado
                        sexo = input("Ingrese el sexo del trabajador a filtrar, h para hombre y m para mujer: ").lower()
                        while not(sexo== 'h' or  sexo== 'm'):
                            print('sexo no valido, recuerde que solo puede ser h para hombre o m para mujer. Intente otra vez')
                            sexo = input("Ingrese el sexo del trabajador a filtrar, h para hombre y m para mujer: ").lower()

                        cargo = input("Ingrese el cargo del trabajador a filtrar, estos pueden ser Asistente, Conductor, Administrativo, Jefe De RRHH, Bodeguero o Ejecutivo: ").title()
                        while not(cargo == 'Asistente' or  cargo == 'Conductor' or cargo == 'Administrativo' or cargo == 'Jefe De RRHH' or cargo == 'Bodeguero' or cargo == 'Ejecutivo'):
                            print('cargo no valido, intente otra vez')
                            cargo = input("Ingrese el cargo del trabajador a filtrar, estos pueden ser Asistente, Conductor, Administrativo, Jefe De RRHH, Bodeguero o Ejecutivo: ").title()

                        area = input("Ingrese el area del trabajador a filtrar, puede ser Soporte, Transporte, Ventas, Marketing, Remuneraciones o Jefatura: ").title()
                        while not(area == 'Soporte' or area == 'Transporte' or area == 'Ventas' or area == 'Marketing' or area == 'Remuneraciones' or area == 'Jefatura'):
                            print('area no valida, recuerde que solo puede ser h para hombre o m para mujer. Intente otra vez')
                            area = input("Ingrese el area del trabajador a filtrar, puede ser Soporte, Transporte, Ventas, Marketing, Remuneraciones o Jefatura: ").title()
                        menu.listar_trabajadores_filtro(crud_tra.obtener(),sexo, cargo, area)
                    if opcion == '4':
                        break
                    if not(opcion == '1' or opcion =='2' or opcion == '3'):
                        print("No ha seleccionado una opcion valida, vuelva a intentarlo")
           
            if rol == 'trabajador':
                while True:
                    #Trabajador puede cambiar: nombre, apellido, sexo, domicilio, teléfono///nombre_completo_emergencia, relación, telefono_emergencia.
                    #Agregar Cargas familiares: rut_carga, rut_trabajador, nombre_completo carga, parentesco, sexo.
                    print ("""
                    1) Ver datos personales
                    2) Modificar datos personales
                    3) Modificar contacto de emergencia
                    4) Agregar Cargas Familiares
                    5) Ver Cargas Familiares
                    6) Cerrar Sesión
                    """)
                    opcion = input("Elija una opción: ")
                    if opcion=='1':
                        print('')
                        #Se obtiene rut del trabajador asociado a la cuenta de usuario para luego consultar la BD
                        rut= usuario.obtener_trabajador().obtener_rut_trabajador()
                        menu.listar_propio_trabajador(crud_tra.obtener(),rut)
                    if opcion=='2':
                        print('')
                        print('A continuacion se mostraran sus datos personales actuales, de estos solo puede modificar su nombre, apellido, sexo, domicilio y/o telefono')
                        menu.listar_datos_personales(crud_tra.obtener(), usuario.obtener_trabajador().obtener_rut_trabajador())
                        menu.cambiar_datos_personales(crud_tra, usuario.obtener_trabajador().obtener_rut_trabajador())
                        print(' ')
                        print('A continuacion se mostraran sus datos personales actualizados: ')
                        menu.listar_datos_personales(crud_tra.obtener(), usuario.obtener_trabajador().obtener_rut_trabajador())

                    if opcion =='3':
                        print('')
                        print('A continuacion se mostraran los datos de su contacto de emergencia')
                        menu.listar_datos_emergencia(crud_tra.obtener(), usuario.obtener_trabajador().obtener_rut_trabajador())
                        menu.cambiar_datos_emergencia(crud_tra, usuario.obtener_trabajador().obtener_rut_trabajador())
                        print(' ')
                        print('A continuacion se mostraran sus datos de emergencia actualizados: ')
                        menu.listar_datos_emergencia(crud_tra.obtener(), usuario.obtener_trabajador().obtener_rut_trabajador())

                    if opcion=='4':
                        rut= usuario.obtener_trabajador().obtener_rut_trabajador()
                        menu.crear_carga(crud_car, rut)
                    

                    if opcion=='5':
                        rut= usuario.obtener_trabajador().obtener_rut_trabajador()
                        menu.listar_cargas(crud_car.obtener(), rut)

                    if opcion =='6':
                        break
                        
        else:
            print('Clave no válida!')