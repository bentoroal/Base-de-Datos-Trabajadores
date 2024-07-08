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
domicilio varchar(100) not null,
telefono int(10) not null,
cargo varchar(20) not null,
fecha_ingreso date not null,
area varchar(20) not null,
dpto varchar(20) not null,
nombre_completo_emergencia varchar(50) not null,
relacion varchar(20) not null,
telefono_emergencia int(10) not null
);


-- Tabla de Cargas Familiares
drop table if exists cargas_familiares;
create table cargas_familiares (
rut_carga varchar(10) primary key,
rut_trabajador varchar(10) not null,
nombre_completo_carga varchar(50) not null,
parentesco varchar(20) not null,
sexo varchar(10) not null,
foreign key (rut_trabajador) references trabajador(rut_trabajador)
);

-- Tabla rol
drop table if exists rol;
create table rol (
id_rol int auto_increment primary key,
nombre_rol varchar(30) not null,
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
INSERT INTO trabajador VALUES('10319622-1', 'Carmen', 'Alvarado', 'm', 'Claudio Vicuña 3910, Quinta Normal, Region Metropolitana', 58496321, 'Asistente', "2020-10-15", 'Ventas', 'Atencion meson', 'Isaac Toro Alvarado', 'hijo', 45125689);
INSERT INTO trabajador VALUES('9039840-7', 'Juan', 'Toro', 'h', 'Ancud 327, San Bernardo, Region Metropolitana', 65458126, 'Conductor', "2010-01-10", 'Transporte', 'Entregas', 'Claudia Toro Alvarado', "hija", 65127812 );
INSERT INTO trabajador VALUES('18432717-1', 'David', 'Morales', 'h', 'Manuel Bustos Huerta 3300, Temuco, Region de la Araucania',63223366,'Administrativo', "2022-12-13", 'Remuneraciones', 'Recursos Humanos', 'Jeannette Segovia Oyarzo', "madre", 12316545);
INSERT INTO trabajador VALUES('18094955-0', 'Benjamin', 'Toro', 'h', 'Manuel Bustos Huerta 3300, Temuco, Region de la Araucania',54899794, 'Jefe de RRHH', "2023-05-28", 'Jefatura', 'Recursos Humanos', 'Ruben Toro Alvarado', 'hermano', 78984562);
INSERT INTO trabajador VALUES('17654453-6', 'Esteban', 'Guerrero', 'h', 'Caupolican 1321, Temuco, Region de la Araucania',96547898, 'Bodeguero', "2023-10-28", 'Soporte', 'Operaciones', 'Maria de las Nieves', 'madre', 68984562);
INSERT INTO trabajador VALUES('12654897-5', 'Elisa', 'Godoy', 'm', 'Javiera Carrera 98, Temuco, Region de la Araucania',65234578, 'Ejecutivo', "2023-06-28", 'Marketing', 'Marketing', 'Jose Paredes', 'hermano', 65457898);
INSERT INTO trabajador VALUES('16319622-1', 'Graciela', 'Alvarado', 'h', 'Claudio Vicuña 3910, Quinta Normal, Region Metropolitana', 65781245, 'Asistente', "2020-10-15", 'Ventas', 'Atencion meson', 'Isaac Toro Alvarado', 'sobrino', 45125689);
commit;


-- Cargas Familiares de muestra:
INSERT INTO cargas_familiares VALUES('19161237-K', '10319622-1', 'Ruben Toro Alvarado', 'hijo', 'h');
INSERT INTO cargas_familiares VALUES('20329565-0', '10319622-1', 'Claudia Toro Alvarado', 'hija', 'm');
INSERT INTO cargas_familiares VALUES('16616845-7', '9039840-7', 'Juan Toro Alvarado', 'hijo', 'm');
INSERT INTO cargas_familiares VALUES('28465123-k', '18432717-1', 'Dominico Toro Segovia', 'hijo', 'h');
INSERT INTO cargas_familiares VALUES('29623354-1', '18094955-0', 'Rocio Toro Segovia', 'hija', 'm');
commit;
 
-- Roles de MUESTRA:
INSERT INTO rol(nombre_rol, descripcion) VALUES('trabajador', 'Trabajador generico de la empresa');
INSERT INTO rol(nombre_rol, descripcion) VALUES('funcionario_rrhh', 'Trabajador de de recursos humanos de la empresa');
INSERT INTO rol(nombre_rol, descripcion) VALUES('jefe_rrhh', 'Jefe del area de RRHH de la empresa');



INSERT INTO usuario VALUES('btoro', '5cbc93d5a9bb424ce5ec387b67b8a27a', 'Benjamin', 'Toro', 1,'18094955-0');
INSERT INTO usuario VALUES('dmorales', '89f71c4e9055ee73c3bc372528a54b9c', 'David', 'Morales', 2,'18432717-1');
INSERT INTO usuario VALUES('calvarado', '49f14ca5d4f5f66bcba10110bd965eb9', 'Carmen', 'Alvarado', 3,'10319622-1');


-- Usuarios de muestra
-- Trabajador usuario: btoro clave: trab
-- Trabajador RRHH usuario:dmorales clave: rrhh
-- Jefe RRHH usuario:calvarado clave: jrrhh
 
