from User import User

class Users :
    users_ids = [] #liste des IDs de TOUS les utilisateurs
    users = []
    
    @staticmethod
    def create_new_user(self) :
        self.users_ids.append(len(self.users))
        user = User(len(self.users))
        self.users.append(user)

    @staticmethod
    def return_user(self, id:int) -> User :
        index = self.users_ids.index(id)
        return self.users[index]