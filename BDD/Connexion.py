import os
import psycopg2
from psycopg2.extras import RealDictCursor
from utils.singleton import Singleton
from dotenv import load_dotenv, find_dotenv


class DBConnection(metaclass=Singleton):
    """
    Classe technique pour ouvrir une seule connexion à la base de données.
    """

    def __init__(self):
        """
        Initialise une connexion à la base de données en utilisant les variables d'environnement.

        :raises: psycopg2.OperationalError si la connexion à la base de données échoue.
        """
        # Ouvre la connexion.
        load_dotenv(find_dotenv())
        self.__connection = psycopg2.connect(
            host=os.environ["HOST"],
            port=os.environ["PORT"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor,
        )

    @property
    def connection(self):
        """
        Renvoie la connexion ouverte.

        :return: La connexion ouverte.
        """
        return self.__connection
