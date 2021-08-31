/*
CREATE DATABASE pruebas;
USE pruebas;

CREATE TABLE Personas(
id int primary key not null auto_increment,
documento varchar(20) unique,
tipo_documento enum("DNI", "CE", "PASAPORTE", "SIN DOCUMENTO"),
nombre varchar(25)  not null,
apellido varchar(50) not null,
correo varchar(100) unique not null,
sexo enum("FEMENINO", "MASCULINO", "OTRO") not null,
fecha_nacimiento date
)

INSERT INTO personas (documento, tipo_documento, nombre, apellido, correo, sexo, fecha_nacimiento)
VALUES ("02897041", "DNI", "MARIO", "MEDINA", "mariomedinam@gmail.com", "MASCULINO", "1977-09-02");

INSERT INTO personas (documento, tipo_documento, nombre, apellido, correo, sexo, fecha_nacimiento)
VALUES ("02898411", "DNI", "ROSA", "BENITES", "rosybenites@gmail.com", "FEMENINO", "1977-08-30");

INSERT INTO personas (documento, tipo_documento, nombre, apellido, correo, fecha_nacimiento, sexo)
VALUES                 (null, 'SIN DOCUMENTO', 'JUAN', 'MARTINEZ', 'jmartinez@gmail.com', '1989-05-15', 'OTRO');

INSERT INTO personas (documento, tipo_documento, nombre, apellido, correo, fecha_nacimiento, sexo)
VALUES                 ('12345678', 'CE', 'MARIA', 'PEREZ', 'mperez@gmail.com', '1995-12-10', 'FEMENINO');


SELECT * FROM personas;

SELECT * FROM personas WHERE nombre = "ROSA";

CREATE TABLE historial_vacunaciones(
id int primary key not null auto_increment,
vacuna enum("PFIZER", "MODERNA", "SINOPHARN") not null,
lote varchar(20),
fecha date,
medico_id int,
paciente_id int,
foreign key(medico_id) references medicos(id),
foreign key(paciente_id) references personas(id)
)
	
create table medicos(
	id int primary key not null auto_increment,
    cmp varchar(5) unique not null,
    nombre varchar(30),
    apeliido varchar(50)
);
*/

INSERT INTO medicos (cmp, nombre, apeliido)
values				("1234", "NOMBRE MEDICO 1"	, "APELIIDO MEDICO 1"),
					("5678", "NOMBRE MEDICO 2"	, "APELIIDO MEDICO 2"),
					("9012", "NOMBRE MEDICO 3"	, "APELIIDO MEDICO 3");
                    
INSERT INTO historial_vacunaciones (vacuna, lote, medico_id, paciente_id, fecha) 
VALUES                                ('PFIZER','1234',1, 1, '2021-07-24'),
                                   ('SINOPHARN','1598', 2, 2, '2021-08-01'),
                                   ('MODERNA','1959', 1, 5, '2021-08-24'),
                                   ('PFIZER','1234',1, 1, now()),
                                   ('SINOPHARN', '5948', 3, 2, now());                    