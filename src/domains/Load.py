class Load:

    """ Crée une instance de TruckManager avec un camion donné et initialise les attributs nécessaires, 
    comme les listes de boîtes à charger, les boîtes déjà chargées, et les compteurs de poids et de volume."""
    def __init__(self, truck):
        self.truck = truck
        self.box=[]
        self.loaded_boxes = []
        self.total_weight = 0
        self.total_volume = 0

## Cette méthode est essentielle pour s'assurer que le camion ne soit pas surchargé
    def can_load_box(self, box):
        """Vérifie si la boîte peut être chargée dans le camion."""
        return (self.total_weight + box.weight <= self.truck.max_weight and
                self.total_volume + box.volume <= self.truck.max_volume)
  
  ## Cette méthode exécute le chargement réel d'une boîte dans le camion. Si la boîte ne peut pas être chargée 
    def add_box(self, box):
        """Ajoute un colis à la liste des colis à charger."""
        self.boxes.append(box)


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


    def load_box(self, box):
        """Charge la boîte dans le camion si possible."""
        if self.can_load_box(box):
            self.loaded_boxes.append(box)
            self.total_weight += box.weight
            self.total_volume += box.volume
            print(f"Box {box.id} of type '{box.type}' loaded into the truck.")
            return True
        print(f"Cannot load Box {box.id}: exceeds truck capacity.")
        return False
    
    def current_load_status(self):
        """Affiche l'état actuel du chargement."""
        print(f"Total weight: {self.total_weight} / {self.truck.max_weight}")
        print(f"Total volume: {self.total_volume} / {self.truck.max_volume}")
        print(f"Loaded boxes: {[box.id for box in self.loaded_boxes]}")
        remaining_weight = self.truck.max_weight - self.total_weight
        remaining_volume = self.truck.max_volume - self.total_volume
        print(f"Remaining weight capacity: {remaining_weight}")
        print(f"Remaining volume capacity: {remaining_volume}")

    def view_boxes(self):
        """Affiche toutes les boîtes en attente de chargement."""
        print("Boxes in loading queue:")
        for box in self.boxes:
            print(f"Box ID: {box.id}, Type: {box.type}, Weight: {box.weight}, Volume: {box.volume}, Priority: {box.priority}, Delivery Time: {box.delivery_time}")

  