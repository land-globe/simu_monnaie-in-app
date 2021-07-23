
from Covoit import Covoit


class User :
    '''Description d'un utlisateur'''
    def __init__(self, new_id):
        self.id = new_id
        self.name = ""
        self.level = "Débutant" # Level : "débutant", "intermédiaire", "expérimenté", "pro"
        self.money = 0
        self.car = ""
        self.places = 0
        self.accept_boards = False
        self.quiver = 0
        self.covoit:Covoit 
    
    def set_infos(self, name:str, level:str, quiver:int):
        self.name = name
        self.level = level
        self.quiver = quiver
    
    def award(self, amount) :
        self.monney += amount
    

    def createCovoit(self, start_location, start_time, spot_id, surfboards, max_surfboards_height, levels, places_available) :
        self.covoit = Covoit()
        self.covoit.save_covoit(start_location, start_time, spot_id, surfboards, max_surfboards_height, levels, places_available)
