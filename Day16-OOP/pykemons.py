from pykemonList import pykemons_dict
from prettytable import PrettyTable
import numpy as np

#First lets define the pykemon class (InPascalCase)
class  Pykemon():

    #The following function will be runned each time a new object of the class is created
    def __init__(self, name_:str, alias_:str=None):    #lvl:int=1, means that lvl must be an integer; and if not passed \\
                                                                #when called it's set to 1
        #The following are the attributes (characteristics) of the object
        self.name = name_    
        self.alias = alias_ if alias_ else name_
        pyke_values = pykemons_dict[name_]    #Dictionary containing information about the pykemon
        self.__type = pyke_values["type"]   #The "__" before "name" makes it a semi-private attribute
        self.__attackPower = pyke_values["attackpower"]
        self.__defense = pyke_values["defense"]
        self.__health = pyke_values["defense"]
    
    def print_statistics(self):
        '''
        Prints pykemon statistics.
        '''
        table = PrettyTable(field_names=["Name", "Type", "Attack Power", "Defense"])
        table.add_row([self.name, self.__type, self.__attackPower, self.__defense])
        print("\n",table,"\n")
    
    def atribs(self):
        '''
        Returns pykemons atributtes in a list as [name, type, attackpower, defense].
        '''
        return [self.name, self.__type, self.__attackPower, self.__defense]
    
    def health(self):
        '''
        Returns pykemon health
        '''
        return self.__health
    
    def defends(self,oponentAttackPower, oponentType):
        '''
        Pykemon recieves an attack.
        '''
        typePenalty = 1
        self.__health -= oponentAttackPower*typePenalty

    def attacks(self,pykemon_to_attack):
        '''
        Pykemon attacks.
        '''
        pykemon_to_attack.defends(self.__attackPower, self.__type)


#Analogously with the trainer class
class Trainer():
    def __init__(self, name_):
        self.name = name_
        self.pykemons = []
        print(f"Trainer {self.name} was created!")

    def add_pykemon(self, pykemon):
        '''
        Adds "pykemon" to the pykemon set of the trainer.
        '''
        self.pykemons.append(pykemon)

    def print_trainer_pykemons(self):
        '''
        Prints trainer pykemons and their statistics.
        '''
        if len(self.pykemons):
            print(f"\n{self.name} pykemons are:")
            table = PrettyTable(field_names=["Name", "Type", "Attack Power", "Defense"])
            for pykemon in self.pykemons:
                table.add_row(pykemon.atribs())
            print("\n",table,"\n")
        else:
            print(f"\nTrainer {self.name} has no pykemons.")
    
    def give_random_pykemons(self, n_pykemons):
        '''
        Gives the trainer a radom set of "n_pykemons" pykemons.
        '''
        rand_indx = np.random.randint(0, len(pykemons_dict),size=n_pykemons)
        for indx in rand_indx:
            pykemon_to_add = Pykemon(list(pykemons_dict.keys())[indx])
            self.add_pykemon(pykemon_to_add)

def test():
    #Select 2 random pykemons
    randInt = np.random.randint(0,len(pykemons_dict))
    pykemon1 = Pykemon(list(pykemons_dict.keys())[randInt])

    randInt = np.random.randint(0,len(pykemons_dict))
    pykemon2 = Pykemon(list(pykemons_dict.keys())[randInt])

    #Create a trainer with no pykemons and show it pykemons
    trainer1 = Trainer(name_="Pepiko")
    trainer1.print_trainer_pykemons()

    #Create a trainer with 2 pykemons and show them
    trainer2 = Trainer(name_="Wanito")
    trainer2.add_pykemon(pykemon1)
    trainer2.add_pykemon(pykemon2)
    trainer2.print_trainer_pykemons()
