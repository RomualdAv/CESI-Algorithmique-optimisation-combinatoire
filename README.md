# CESI-Algorithmique-optimisation-combinatoire
 
A la suite d'un appel d'offre lancé par l’ADEME *(Agence de l’Environnement et de la Maîtrise de l’Energie)*, nous avons pour objectif de participer au developpement de méthodes de transport plus économes et plus écologique. Notre équipe se focalisera ainsi sur l'optimisation des tournées de livraison, part importante des émissions polluantes de la ville.

Globalement, le problème consiste à calculer un itinéraire optimal reliant plusieurs villes tout en prenant en compte differents éléments comme la durée de trajet, le type de marchandise etc... La solution recherchée doit s’appuyer sur des techniques de Recherche Opérationnelle et proposer un algorithme capable de gérer des instances de grande taille *(jusqu'à plusieurs milliers de villes)*. Le projet inclut également la possibilité d’ajouter des contraintes supplémentaires pour rendre une solution des plus optimales; comme des fenêtres de temps, la gestion de plusieurs camions ou des variations de trafic.


- Fenêtre de temps de livraison pour chaque objet
    - Interdiction de livrer hors de la fenêtre
    - Possibilité d'attendre sur place l'ouverture de la fenêtre temporelle

- k camions disponibles simultanément pour effectuer les livraisons. Le calcul de la tournée devra inclure l’affectation des objets (et donc des points de livraison) aux différents camions disponibles, et minimiser non plus le temps total, mais la date de retour du dernier camion à la base.
    - Capacité des camions *(3 dimension)* et encombrement des objets
    - Certains objets ne peuvent être livrés que par certains camions

- Chaque objet a un point de collecte spécifique

- Le temps de parcours d’une arête varie au cours du temps (ce qui revient à faire varier sa longueur), pour représenter la variation du trafic

- La solution proposée devra gérer des instances de grande taille *(jusqu'à plusieurs milliers de villes)*