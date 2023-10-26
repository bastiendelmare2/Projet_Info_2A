DROP SCHEMA IF EXISTS Projet_Info2A CASCADE;
CREATE SCHEMA Projet_Info2A;

--------------------------------------------------------------
-- Carburants
--------------------------------------------------------------

DROP TABLE IF exists Projet_Info2A.carburants CASCADE ;
CREATE TABLE Projet_Info2A.carburants (
    nom_carbu_carbu serial PRIMARY KEY,
    nom_ text
);