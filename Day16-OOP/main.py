from pykemons import Pykemon, Trainer
n_pyk = 4

#Create two trainers with four random pykemons each
pepiko = Trainer(name_="Pepiko")
pepiko.give_random_pykemons(n_pykemons=n_pyk)
pepiko.print_trainer_pykemons()

wanito = Trainer(name_="Wanito")
wanito.give_random_pykemons(n_pykemons=n_pyk)
wanito.print_trainer_pykemons()

#Lets design an example battle
indx=-1
while indx not in range(n_pyk):
    indx = int(input("Which pykemon do you select for trainer pepiko? Give its index (starting at 0):"))    
pepikos_pykemon = pepiko.pykemons[indx]

indx=-1
while indx not in range(n_pyk):
    indx = int(input("Which pykemon do you select for trainer wanito? Give its index (starting at 0):"))
wanitos_pykemon = wanito.pykemons[indx]

pepikos_pykemon.print_statistics()
wanitos_pykemon.print_statistics()

pepikos_pykemon.attacks(wanitos_pykemon)
print(f"{pepikos_pykemon.name} attacks {wanitos_pykemon.name}.\n {wanitos_pykemon.name}'s health has been reduced to {wanitos_pykemon.health()}.")