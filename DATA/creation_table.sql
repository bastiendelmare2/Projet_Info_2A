CREATE SCHEMA projet2a


----------------------------------------------------------------------
---  UTILISATEUR ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Utilisateur

CREATE TABLE projet2a.Utilisateur (
    id_utilisateur SERIAL PRIMARY KEY,
    nom_utilisateur VARCHAR(255) NOT NULL,
    prenom_utilisateur VARCHAR(255) NOT NULL,
    age INT,
    mdp_utilisateur VARCHAR(255) NOT NULL
);

----------------------------------------------------------------------
---  STATIONSSERVICES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.StationsServices

CREATE TABLE projet2a.StationsServices (
    id_stations VARCHAR(255) PRIMARY KEY,
    adresse VARCHAR(255) NOT NULL,
    ville VARCHAR(255) NOT NULL
);


----------------------------------------------------------------------
---  TYPECARBURANTS ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.TypeCarburants

CREATE TABLE projet2a.TypeCarburants (
    id_typecarburants SERIAL PRIMARY KEY,
    nom_type_carburants VARCHAR(255) NOT NULL
);

----------------------------------------------------------------------
---  COMPTEUTILISATEUR ---
----------------------------------------------------------------------

DROP TABLE IF EXISTS projet2a.CompteUtilisateur

CREATE TABLE projet2a.CompteUtilisateur (
    id_compte SERIAL PRIMARY KEY,
    mdp VARCHAR(255) NOT NULL,
    identifiant VARCHAR(255) NOT NULL
);



----------------------------------------------------------------------
---  PRIXCARBURANTS ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.PrixCarburants

CREATE TABLE projet2a.PrixCarburants (
    id_prix SERIAL PRIMARY KEY,
    station_id VARCHAR(255) NOT NULL,
    typecarburant_id INT NOT NULL,
    prix FLOAT NOT NULL,
    FOREIGN KEY (station_id) REFERENCES projet2a.StationsServices(id_stations),
    FOREIGN KEY (typecarburant_id) REFERENCES projet2a.TypeCarburants(id_typecarburants)
);

----------------------------------------------------------------------
---  SERVICES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Services

CREATE TABLE projet2a.Services (
    id_services SERIAL PRIMARY KEY,
    nom_services VARCHAR(255) NOT NULL,
    id_stations VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES projet2a.StationsServices(id_stations)
);


----------------------------------------------------------------------
---  HORAIRES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Horaires

CREATE TABLE projet2a.Horaires (
    id_stations VARCHAR(255) NOT NULL,
    horaire TIME NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES projet2a.StationsServices(id_stations)
);

----------------------------------------------------------------------
---  COORDONNEES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Coordonnees

CREATE TABLE projet2a.Coordonnees (
    id_stations VARCHAR(255) NOT NULL,
    longitude DECIMAL(10, 6) NOT NULL,
    latitude DECIMAL(10, 6) NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES projet2a.StationsServices(id_stations)
);

----------------------------------------------------------------------
---  STATIONS_TO_STATIONSPREFEREES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Stations_to_StationsPreferees

CREATE TABLE projet2a.Stations_to_StationsPreferees (
    id_stations VARCHAR(255) NOT NULL,
    id_stations_pref VARCHAR(255),
    FOREIGN KEY (id_stations) REFERENCES projet2a.StationsServices(id_stations)
);

----------------------------------------------------------------------
---  STATIONSPREFEREES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.StationsPreferees

CREATE TABLE projet2a.StationsPreferees (
    id_stations_pref SERIAL PRIMARY KEY,
    id_utilisateur INT NOT NULL,
    FOREIGN KEY (id_utilisateur) REFERENCES projet2a.Utilisateur(id_utilisateur)
);


