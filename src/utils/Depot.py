class Depot:
    def __init__(self, location, name, possibility_of_parking, delivery_window, road_list):
        self.location = location 
        self.name= name
        self.delivery_window= delivery_window # fenetre de livraison
        self.possibility_of_parking= possibility_of_parking # possibilite de se garer en bool
        self.road_list= road_list # liste des routes (tuple entiers) 

    def __str__(self):
        return f"Depot : {self.name}, Location: {self.location}, Parking:{ 'Yes' if self.possibility_of_parking else 'No'}, Delivery window: {self.delivery_window}"
    
       