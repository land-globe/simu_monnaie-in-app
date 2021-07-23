from User import User
from Users import Users
import datetime

#On creer 4 users
Users.create_new_user()
Users.create_new_user()
Users.create_new_user()
Users.create_new_user()

yann:User = Users.return_user(0)
nico = Users.return_user(1)
antman = Users.return_user(2)
hugo = Users.return_user(3)

yann.set_infos("Yann", "Expérimenté", 3)
nico.set_infos("Nico", "Pro", 1)
antman.set_infos("Antman", "Débutant", 0)
hugo.set_infos("Hugo", "Pro", 1)

yann.createCovoit("Bordeaux", datetime.date, 1, 4, "7\"8", ["Débutan", ""])