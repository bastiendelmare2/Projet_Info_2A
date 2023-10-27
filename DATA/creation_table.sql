DROP SCHEMA IF EXISTS Projet2A CASCADE;
CREATE SCHEMA Projet2A


----------------------------------------------------------------------
---  UTILISATEUR ---
----------------------------------------------------------------------

CREATE TABLE Utilisateur (
    id_utilisateur SERIAL PRIMARY KEY,
    nom_utilisateur VARCHAR(255) NOT NULL,
    prenom_utilisateur VARCHAR(255) NOT NULL,
    age INT,
    mdp_utilisateur VARCHAR(255) NOT NULL
);

----------------------------------------------------------------------
---  STATIONSSERVICES ---
----------------------------------------------------------------------

CREATE TABLE StationsServices (
    id_stations VARCHAR(255) PRIMARY KEY,
    adresse VARCHAR(255) NOT NULL,
    ville VARCHAR(255) NOT NULL
);


----------------------------------------------------------------------
---  TYPECARBURANTS ---
----------------------------------------------------------------------

CREATE TABLE TypeCarburants (
    id_typecarburants SERIAL PRIMARY KEY,
    nom_type_carburants VARCHAR(255) NOT NULL
);


----------------------------------------------------------------------
---  PRIXCARBURANTS ---
----------------------------------------------------------------------

CREATE TABLE PrixCarburants (
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

CREATE TABLE Services (
    id_services SERIAL PRIMARY KEY,
    nom_services VARCHAR(255) NOT NULL,
    id_stations VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES StationsServices(id_stations)
);


----------------------------------------------------------------------
---  HORAIRES ---
----------------------------------------------------------------------

CREATE TABLE Horaires (
    id_stations VARCHAR(255) NOT NULL,
    horaire TIME NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES StationsServices(id_stations)
);

----------------------------------------------------------------------
---  COORDONNEES ---
----------------------------------------------------------------------

CREATE TABLE Coordonnees (
    id_stations VARCHAR(255) NOT NULL,
    longitude DECIMAL(10, 6) NOT NULL,
    latitude DECIMAL(10, 6) NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES StationsServices(id_stations)
);

----------------------------------------------------------------------
---  STATIONS_TO_STATIONSPREFEREES ---
----------------------------------------------------------------------

CREATE TABLE Stations_to_StationsPreferees (
    id_stations VARCHAR(255) NOT NULL,
    id_stations_pref VARCHAR(255),
    FOREIGN KEY (id_stations) REFERENCES StationsServices(id_stations)
);

----------------------------------------------------------------------
---  STATIONSPREFEREES ---
----------------------------------------------------------------------
CREATE TABLE StationsPreferees (
    id_stations_pref SERIAL PRIMARY KEY,
    id_utilisateur INT NOT NULL,
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateur(id_utilisateur)
);


