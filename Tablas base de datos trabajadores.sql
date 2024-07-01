drop database if exists programa_trabajadores_db;
create database programa_trabajadores_db;
use programa_trabajadores_db;

-- Tabla trabajadores
drop table if exists trabajador;
create table trabajador (
rut_trabajador varchar(10) primary key,
nombre_trabajador varchar(15) not null,
apellido_trabajador varchar(15) not null,
sexo varchar(1) not null,
domicilio varchar(30),
telefono int(10)
);

-- Tabla de Datos Laborales
drop table if exists datos_laborales;
create table datos_laborales (
rut_trabajador varchar(10) primary key,
cargo varchar(20) not null,
fecha_ingreso date not null,
area varchar(20) not null,
dpto varchar(20) not null,
foreign key (rut_trabajador) references trabajador(rut_trabajador)
);

-- Tabla de Datos de Emergencia
drop table if exists datos_emergencia;
create table datos_emergencia (
rut_trabajador varchar(10) primary key,
nombre_completo_emergencia varchar(50) not null,
relacion varchar(20),
telefono_emergencia int(10) not null,
foreign key (rut_trabajador) references trabajador(rut_trabajador)
);

-- Tabla de Cargas Familiares
drop table if exists cargas_familiares;
create table cargas_familiares (
rut_carga varchar(10) primary key,
rut_trabajador varchar(10) not null,
nombre_completo_carga varchar(50) not null,
parentesco varchar(20),
sexo varchar(10),
foreign key (rut_trabajador) references trabajador(rut_trabajador)
);

-- Tabla rol
drop table if exists rol;
create table rol (
id_rol int auto_increment primary key,
nombre_rol varchar(15) not null,
descripcion varchar(50)
);

-- Tabla de usuarios
drop table if exists usuario;
create table usuario (
nombre_usuario varchar(15) primary key,
hash_clave varchar(32) not null,
nombre varchar(50),
apellido varchar(50),
id_rol int not null,
rut_trabajador varchar(10),
foreign key (id_rol) references rol (id_rol),
foreign key (rut_trabajador) references trabajador (rut_trabajador),
unique key (rut_trabajador)
);

-- Trabajadores de muestra
INSERT INTO trabajador VALUES('10319622-1', 'Carmen', 'Alvarado', 'm', 'Claudio Vicuña 3910', 58496321);
INSERT INTO trabajador VALUES('9039840-7', 'Juan', 'Toro', 'h', 'Ancud 327', 65458126 );
INSERT INTO trabajador VALUES('18432717-1', 'David', 'Morales', 'h', 'Manuel Bustos Huerta 3300',63223366);
INSERT INTO trabajador VALUES('18094955-0', 'Benjamin', 'Toro', 'h', 'Manuel Bustos Huerta 3300',54899794);
commit;

-- Datos Laborales de muestra:
INSERT INTO datos_laborales VALUES('10319622-1','Asistente', "2020-10-15", 'Ventas', 'Atencion meson');
INSERT INTO datos_laborales VALUES('9039840-7','Conductor', "2010-01-10", 'Transporte', 'Entregas');
INSERT INTO datos_laborales VALUES('18432717-1','Administrativo', "2022-12-13", 'Remuneraciones', 'Recursos Humanos');
INSERT INTO datos_laborales VALUES('18094955-0','Jefe de RRHH', "2023-05-28", 'Jefatura', 'Recursos Humanos');
commit;

-- Datos de Emergencia de muestra:
INSERT INTO datos_emergencia VALUES('10319622-1','Isaac Toro Alvarado', 'hijo', 45125689);
INSERT INTO datos_emergencia VALUES('9039840-7','Claudia Toro Alvarado', "hija", 65127812);
INSERT INTO datos_emergencia VALUES('18432717-1','Jeannette Segovia Oyarzo', "madre", 12316545);
INSERT INTO datos_emergencia VALUES('18094955-0','Ruben Toro Alvarado', 'hermano', 78984562);
commit;

-- Cargas Familiares de muestra:
INSERT INTO cargas_familiares VALUES('19161237-K', '10319622-1', 'Ruben Toro Alvarado', 'hijo', 'h');
INSERT INTO cargas_familiares VALUES('20329565-0', '10319622-1', 'Claudia Toro Alvarado', 'hija', 'm');
INSERT INTO cargas_familiares VALUES('16616845-7', '9039840-7', 'Juan Toro Alvarado', 'hijo', 'm');
INSERT INTO cargas_familiares VALUES('28465123-k', '18432717-1', 'Dominico Toro Segovia', 'hijo', 'h');
INSERT INTO cargas_familiares VALUES('29623354-1', '18094955-0', 'Rocio Toro Segovia', 'hija', 'm');
commit;
 
 -- FALTAN DATOS DE MUESTRA
