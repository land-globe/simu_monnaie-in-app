from user_class import User
# from Users import Users
import datetime

#On creer 4 users
yann = User(0)
nico = User(1)
antman = User(2)
hugo = User(3)

yann.set_infos("Yann", "Expérimenté", 3)
nico.set_infos("Nico", "Pro", 1)
antman.set_infos("Antman", "Débutant", 0)
hugo.set_infos("Hugo", "Pro", 1)

yann.createCovoit("Bordeaux", datetime.date, 1, 4, "7\"8", ["Débutant", "Intermediaire", "Expérimenté"], 4)
yann.covoit.add_surfer(2)
# yann.covoit.add_surfer(3)
yann.terminateCovoit()

print(yann.money)