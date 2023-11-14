from BDD.DAO_Reset_Tables import SuppressionDonnees
from Alimtentation import Alimentation
from METIER.Importation import XML

SuppressionDonnees.supprimer_donnees_tables()
Alimentation.alimenter_toutes_tables(XML())