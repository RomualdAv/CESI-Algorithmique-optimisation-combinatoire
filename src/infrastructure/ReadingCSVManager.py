from src.utils.Box import Box
from src.utils.Truck import Truck
from src.infrastructure.CSVManager import CsvManager


def readBoxSinceCsv ( chemin_dossier, nom_fichier)

    """
        Fonction pour lire les boîtes depuis un fichier CSV et retourner une liste d'objets Box.

        :param chemin_dossier: Chemin vers le dossier du fichier CSV
        :param nom_fichier: Nom du fichier CSV
        :return: Liste d'objets Box
        :raises CsvError: si le fichier ne peut pas être lu
    """

    try: 
        csv_Manger= CsvManager(chemin_dossier, nom_fichier)
        boites= []

         #Lire toutes les lignes du fichier CSV, en ignorant la première ligne si elle contient des en-têtes

        with open( csv_manager.directory, mode='r', newLine='',encoding='utf-8') as f:

            reader = csv.reader(f)
            next(reader) # ignore l'entete
            
            for ligne in reader: # conversion des lignes en objets
                boite= box( 
                    id= ligne[0],
                    type= ligne[1],
                    start= ligne[2],
                    end= ligne[3]
                    size= float(ligne[4])

                )
                boite.append(boite)
            return boites
    except CsvError as e:
        print(e)
    return []    

def readBoxSinceCsv(chemin_dossier, nom_fichier)
    try: 
        csv_manager= CsvManger( chemin_dossier, nom_fichier)
        camions=[]
        with open (csv_manager.dierectory, mode='r', newline='', encoding='utf_8') as f:
            reader = csv.reader(f)
            next(reader)
            for ligne in reader:
                camion= Truck(
                    id= ligne[0],
                    type= ligne[1],
                    max_capacity= float(ligne[2]),
                    current_capacity= float( ligne[3])
                                        
                )
                camions.append(camion)
            return camions
    except CsvError as e:
        print(e)
        return []
   