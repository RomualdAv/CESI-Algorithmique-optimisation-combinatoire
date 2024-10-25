class Load:
    def __init__(self, truck):
        self.truck = truck
        self.loaded_boxes = []
        self.total_weight = 0
        self.total_volume = 0

    def can_load_box(self, box):
        """Vérifie si la boîte peut être chargée dans le camion."""
        return (self.total_weight + box.weight <= self.truck.max_weight and
                self.total_volume + box.volume <= self.truck.max_volume)


    def add_box(self, box):
        """Ajoute un colis à la liste des colis à charger."""
        self.boxes.append(box)

 
    def sort_boxes(self):
        """Trie les colis par ordre de priorité et de temps de livraison."""
        # On trie d'abord par priorité (plus la valeur est basse, plus c'est prioritaire),
        # puis par temps de livraison (plus bas en premier).

        self.boxes.sort(key=lambda box: (box.priority, box.delivery_time))
        
    def load_boxes(self, boxes):
        """Charge les boîtes en tenant compte de leur type et de la capacité du camion."""
        # Trier les boîtes par type, puis par poids et volume
        boxes.sort(key=lambda x: (x.type, x.weight, x.volume))

        for box in boxes:
            if not self.is_truck_full():
                self.load_box(box)
            else:
                print("Truck is full. No more boxes can be loaded.")
             
            break  # Sortir de la boucle si le camion est plein

    def sort_boxes_by_time(self):
        """Trie les colis par ordre de temps de livraison."""
        self.boxes.sort(key=lambda box: box.delivery_time)

    def load_trucks(self, trucks):
        """Charge les colis dans les camions en fonction de la priorité."""
        self.sort_boxes()
        
        for truck in trucks:
            while self.boxes and truck.can_load(self.boxes[0]):
                box = self.boxes.pop(0)  # Prendre le colis le plus prioritaire
                truck.load_box(box)  # Charger le colis dans le camion


    def load_box(self, box):
        """Charge la boîte dans le camion si possible."""
        if self.can_load_box(box):
            self.loaded_boxes.append(box)
            self.total_weight += box.weight
            self.total_volume += box.volume
            print(f"Box {box.id} of type '{box.type}' loaded into the truck.")
        else:
            print(f"Cannot load Box {box.id}: exceeds truck capacity.")

  
    def is_truck_full(self):
        """Vérifie si le camion est plein."""
        return self.total_weight >= self.truck.max_weight or self.total_volume >= self.truck.max_volume

    def remaining_capacity(self):

        """Calcule l'espace restant dans le camion."""
        remaining_weight = self.truck.max_weight - self.total_weight
        remaining_volume = self.truck.max_volume - self.total_volume
        return remaining_weight, remaining_volume

    def unload_box(self, box_id):
        """Décharge la boîte identifiée par box_id."""
        for box in self.loaded_boxes:
            if box.id == box_id:
                self.loaded_boxes.remove(box)
                self.total_weight -= box.weight
                self.total_volume -= box.volume
                print(f"Box {box.id} unloaded from the truck.")
                return
        print(f"Box {box_id} not found in the truck.")

    def current_load_status(self):
        """Affiche l'état actuel du chargement."""
        
        print(f"Total weight: {self.total_weight} / {self.truck.max_weight}")
        print(f"Total volume: {self.total_volume} / {self.truck.max_volume}")
        print(f"Loaded boxes: {[box.id for box in self.loaded_boxes]}")
        remaining_weight, remaining_volume = self.remaining_capacity()
        print(f"Remaining weight capacity: {remaining_weight}")
        print(f"Remaining volume capacity: {remaining_volume}")
