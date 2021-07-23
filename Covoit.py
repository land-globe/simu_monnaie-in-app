from datetime import *
from Users import Users
from User import User

class Covoit :
    '''Description d'un covoit'''
    def __init__(self, user_id):
        self.conductor_id = user_id
        self.conductor:User = Users.return_user(self.conductor_id)
        self.start_location = "" #adresse maps
        self.spot_id = 0
        self.start_time = datetime.timestamp()
        self.surfoards = 0
        self.max_surfboards_height = 0
        self.levels = [] # Levels : "débutant", "intermédiaire", "expérimenté", "pro"
        self.surfers = [] # surfers ids
        self.places_available = 0
        self.published = False
        self.likes = 0

    def save_covoit(self, start_location, start_time, spot_id, surfboards, max_surfboards_height, levels, places_available) :
        ''' Uniquement le condcuteur a accès à cette fonction'''
        self.start_location = start_location
        self.spot_id = spot_id
        self.start_time = start_time
        self.surfoards = surfboards
        self.max_surfboards_height = max_surfboards_height
        self.levels = levels
        self.places_available = places_available
    
    def publish_covoit(self) :
        ''' Uniquement le condcuteur a accès à cette fonction'''
        self.publish = True
    
    def like(self) :
        '''Tout le monde y a accès'''
        self.likes += 1
    
    def add_surfer(self, surfer_id):
        '''
        Uniquement le conducteur pourra avoir accès à cette fonction
        
        le conducteur valide un surfeur
        '''
        self.surfers.append(surfer_id)
        self.places_available -= 1
    
    def cancel_covoit(self) :
        self.publish = False 
        ## On sort tout de la BDD
    
    def terminate_covoit(self) :
        '''Après avoir confirmé que le covoit s'est bien déroulé on récompense le conducteur'''
        award = len(self.surfers)*3 # 3 = la rémunération : 3$ pour chaque personne transportée
        self.conductor.award(award)



