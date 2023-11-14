----------------------------------------------------------------------
---  STATIONSSERVICES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.StationsServices CASCADE

CREATE TABLE projet2a.StationsServices (
    id_stations INT PRIMARY KEY,
    adresse VARCHAR(255) NOT NULL,
    ville VARCHAR(255) NOT NULL
);


----------------------------------------------------------------------
---  TYPECARBURANTS ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.TypeCarburants CASCADE

CREATE TABLE projet2a.TypeCarburants (
    id_typecarburants INT PRIMARY KEY,
    nom_type_carburants VARCHAR(255) NOT NULL
);

----------------------------------------------------------------------
---  COMPTEUTILISATEUR ---
----------------------------------------------------------------------

DROP TABLE IF EXISTS projet2a.CompteUtilisateur CASCADE

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
    id_type_carburant INT,
    id_stations INT,
    prix FLOAT,
    FOREIGN KEY (id_stations) REFERENCES projet2a.StationsServices(id_stations),
    FOREIGN KEY (id_type_carburant) REFERENCES projet2a.TypeCarburants(id_typecarburants),
    PRIMARY KEY (id_type_carburant, id_stations)
);


----------------------------------------------------------------------
---  SERVICES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Services

CREATE TABLE projet2a.Services (
    id_service INT PRIMARY KEY,
    nom_service VARCHAR(255) NOT NULL
);

----------------------------------------------------------------------
---  STATIONS_TO_SERVICES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Stations_to_Services

CREATE TABLE projet2a.Stations_to_Services (
    id_stations INT,
    id_service INT,
    FOREIGN KEY (id_stations) REFERENCES projet2a.StationsServices(id_stations),
    FOREIGN KEY (id_service) REFERENCES projet2a.Services(id_service),
    PRIMARY KEY (id_stations, id_service)
);


----------------------------------------------------------------------
---  HORAIRES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Horaires

CREATE TABLE projet2a.Horaires (
    id_horaires INT PRIMARY KEY,
    horaires VARCHAR(255)
);

----------------------------------------------------------------------
---  COORDONNEES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Coordonnees

CREATE TABLE projet2a.Coordonnees (
    id_stations INT NOT NULL,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    FOREIGN KEY (id_stations) REFERENCES projet2a.StationsServices(id_stations)
);

----------------------------------------------------------------------
---  STATIONS_TO_STATIONSPREFEREES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.Stations_to_StationsPreferees

CREATE TABLE projet2a.Stations_to_StationsPreferees (
    id_stations INT NOT NULL,
    id_stations_pref INT,
    PRIMARY KEY (id_stations, id_stations_pref)
);


----------------------------------------------------------------------
---  STATIONSPREFEREES ---
----------------------------------------------------------------------
DROP TABLE IF EXISTS projet2a.StationsPreferees

CREATE TABLE projet2a.StationsPreferees (
    id_stations_pref INT primary KEY,
    id_compte INT NOT NULL,
    nom VARCHAR (255) NOT null,
    FOREIGN KEY (id_compte) REFERENCES projet2a.CompteUtilisateur(id_compte)
);


