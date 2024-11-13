from random import shuffle, sample, randint, choice

def calculer_distance_totale(chemin, distance_matrix):
    distance_totale = 0
    for i in range(len(chemin) - 1):
        distance_totale += distance_matrix[chemin[i]][chemin[i + 1]]
    return distance_totale

def generer_voisin(chemin, noeuds, choix):
    voisin = chemin[:]
    action = randint(0, 2)  # 0: switch, 1: add, 2: remove
    
    if action == 0 and len(voisin) > 3:  # switch two elements, excluding the first and last
        i, j = sample(range(1, len(voisin) - 1), 2)
        voisin[i], voisin[j] = voisin[j], voisin[i]
    elif action == 1 and len(voisin) < len(noeuds) + 1:  # add a new node, excluding the last
        noeud_a_ajouter = choice([n for n in noeuds if n not in voisin])
        position = randint(1, len(voisin) - 1)
        voisin.insert(position, noeud_a_ajouter)
    elif action == 2 and len(voisin) > len(choix) + 2:  # remove a node, excluding the first and last
        position = randint(1, len(voisin) - 2)
        if voisin[position] not in choix:  # ensure we don't remove mandatory nodes
            voisin.pop(position)
    
    return voisin

def recherche_hill_climbing(distance_matrix, choix, point_depart, max_iterations=90000, tabou_taille=50):
    n = len(distance_matrix)
    noeuds = list(range(n))
    
    # initialisation du chemin qui comprend les noeuds obligatoires
    noeuds_restants = [noeud for noeud in noeuds if noeud not in choix and noeud != point_depart]
    chemin_initial = [point_depart] + list(choix) + noeuds_restants + [point_depart]
    shuffle(chemin_initial[1:-1])  # mélanger les noeuds restants sauf le point de départ et le retour
    
    # calcul de la distance initiale
    meilleur_chemin = chemin_initial
    meilleure_distance = calculer_distance_totale(meilleur_chemin, distance_matrix)
    
    # liste tabou
    tabou = set()
    tabou.add(tuple(meilleur_chemin))
    
    for iteration in range(max_iterations):
        voisin = generer_voisin(meilleur_chemin, noeuds, choix) # voisin aléatoire
        voisin[0] = point_depart  # assurer que le point de départ reste le même
        voisin[-1] = point_depart  # assurer que le point de retour reste le même

        if tuple(voisin) not in tabou:
            distance_voisin = calculer_distance_totale(voisin, distance_matrix)
            if distance_voisin < meilleure_distance:
                meilleur_chemin = voisin
                meilleure_distance = distance_voisin
                tabou.add(tuple(voisin))  # on ajoute le voisin à la liste tabou
                if len(tabou) > tabou_taille:
                    # retirer le premier element de la liste tabou si elle dépasse la taille maximale
                    tabou = set(list(tabou)[1:]) 
                print(f"Iteration {iteration + 1}: Nouvelle meilleure distance trouvée : {meilleure_distance}, Chemin : {meilleur_chemin}")    
    return meilleure_distance, meilleur_chemin