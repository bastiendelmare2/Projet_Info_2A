DROP DATABASE IF EXISTS Projet_Info2A CASCADE;
CREATE DATABASE Projet_Info2A;

--------------------------------------------------------------
-- Carburants
--------------------------------------------------------------

DROP DATABASE IF exists Projet_Info2A.carburants CASCADE ;
CREATE DATABASE Projet_Info2A.carburants (
    nom_carbu_carbu serial PRIMARY KEY,
    nom_ text
);
