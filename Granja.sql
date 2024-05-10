CREATE DATABASE Gestion_Granja;

USE Gestion_Granja;

CREATE TABLE cultivos (
    id INT PRIMARY KEY IDENTITY,
    nombre NVARCHAR(255) NOT NULL,
    tipo NVARCHAR(255) NOT NULL,
    area FLOAT NOT NULL,
    rendimiento FLOAT NOT NULL
);

CREATE TABLE animales (
    id INT PRIMARY KEY IDENTITY,
    especie NVARCHAR(255) NOT NULL,
    raza NVARCHAR(255) NOT NULL,
    edad INT NOT NULL,
    peso FLOAT NOT NULL
);
SELECT * FROM animales;
SELECT * FROM Cultivos;