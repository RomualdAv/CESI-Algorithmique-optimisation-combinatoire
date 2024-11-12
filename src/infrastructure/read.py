from src.utils.Box import Box
from src.utils.Truck import Truck
from src.infrastructure.CSVManager import CsvManager
from src.utils.error import CsvError

def readObjectSinceCsv(csv_manager, type_objet):
    """

    :param csv_manager: Une instance de CsvManager déjà initialisée avec le fichier à lire
    :param type_objet: La classe de l'objet à créer, soit Box, soit Truck
    :return: Une liste d'instances de type_objet
    """
    objets = []
    try:
        # Lire toutes les lignes du fichier CSV
        ligne_index = 0 
        while True:
            try:
                # Lecture d'une ligne à l'index actuel
                ligne = csv_manager.readLine(ligne_index)
                if ligne_index == 0:
                    # Ignorer l'en-tête
                    ligne_index += 1 
                    continue
                if type_objet == Box:
                    objet = Box(
                        id=ligne[0],
                        type=ligne[1],
                        start=ligne[2],
                        end=ligne[3],
                        size=float(ligne[4])
                    )
                elif type_objet == Truck:
                    objet = Truck(
                        id=ligne[0],
                        type=ligne[1],
                        max_capacity=float(ligne[2]),
                        current_capacity=float(ligne[3])
                    )
                else:
                    raise ValueError("Type d'objet non pris en charge.")
                objets.append(objet)
                ligne_index += 1
            except CsvError:
                # Arrête la lecture si on dépasse le nombre de lignes dans le fichier
                break
    except CsvError as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
    return objets
