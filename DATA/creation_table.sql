DROP SCHEMA IF EXISTS Projet2A CASCADE;
CREATE SCHEMA Projet2A


----------------------------------------------------------------------
---  UTILISATEUR ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS Projet2A.Utilisateur

CREATE TABLE Projet2A.Utilisateur (
    id_utilisateur SERIAL PRIMARY KEY,
    nom_utilisateur VARCHAR(255) NOT NULL,
    prenom_utilisateur VARCHAR(255) NOT NULL,
    age INT,
    mdp_utilisateur VARCHAR(255) NOT NULL
);

----------------------------------------------------------------------
---  STATIONSSERVICES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS Projet2A.StationsServices

CREATE TABLE Projet2A.StationsServices (
    id_stations VARCHAR(255) PRIMARY KEY,
    adresse VARCHAR(255) NOT NULL,
    ville VARCHAR(255) NOT NULL
);


----------------------------------------------------------------------
---  TYPECARBURANTS ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS Projet2A.TypeCarburants

CREATE TABLE Projet2A.TypeCarburants (
    id_typecarburants SERIAL PRIMARY KEY,
    nom_type_carburants VARCHAR(255) NOT NULL
);


----------------------------------------------------------------------
---  PRIXCARBURANTS ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS Projet2A.PrixCarburants

CREATE TABLE Projet2A.PrixCarburants (
    id_prix SERIAL PRIMARY KEY,
    station_id VARCHAR(255) NOT NULL,
    typecarburant_id INT NOT NULL,
    prix FLOAT NOT NULL,
    FOREIGN KEY (station_id) REFERENCES StationsServices(id_stations),
    FOREIGN KEY (typecarburant_id) REFERENCES TypeCarburants(id_typecarburants)
);

----------------------------------------------------------------------
---  SERVICES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS Projet2A.Services

CREATE TABLE Projet2A.Services (
    id_services SERIAL PRIMARY KEY,
    nom_services VARCHAR(255) NOT NULL,
    id_stations VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES StationsServices(id_stations)
);


----------------------------------------------------------------------
---  HORAIRES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS Projet2A.Horaires

CREATE TABLE Projet2A.Horaires (
    id_stations VARCHAR(255) NOT NULL,
    horaire TIME NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES StationsServices(id_stations)
);

----------------------------------------------------------------------
---  COORDONNEES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS Projet2A.Coordonnees

CREATE TABLE Projet2A.Coordonnees (
    id_stations VARCHAR(255) NOT NULL,
    longitude DECIMAL(10, 6) NOT NULL,
    latitude DECIMAL(10, 6) NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES StationsServices(id_stations)
);

----------------------------------------------------------------------
---  STATIONS_TO_STATIONSPREFEREES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS Projet2A.Stations_to_StationsPreferees

CREATE TABLE Projet2A.Stations_to_StationsPreferees (
    id_stations VARCHAR(255) NOT NULL,
    id_stations_pref VARCHAR(255),
    FOREIGN KEY (id_stations) REFERENCES StationsServices(id_stations)
);

----------------------------------------------------------------------
---  STATIONSPREFEREES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS Projet2A.StationsPreferees

CREATE TABLE Projet2A.StationsPreferees (
    id_stations_pref SERIAL PRIMARY KEY,
    id_utilisateur INT NOT NULL,
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateur(id_utilisateur)
);


