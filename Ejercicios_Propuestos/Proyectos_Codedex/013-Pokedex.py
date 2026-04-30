
class Pokemon:
    def __init__(self,entry:int,name:str,type:list,description:str,is_caught:bool):
     self.entry = entry
     self.name = name
     self.type = type
     self.description = description
     self.is_caugt = is_caught

    def speak(self):
       print(f'{self.name} {self.name}!')

    def display_details(self):
       print(f'Entry Number: {self.entry}\n Name: {self.name}\n Type: {self.type}\n Description:{self.description}')

pokemon1 = Pokemon(25,'Pikachu',['Electric'],'Pikachu es un pokemon lindo',True) 
pokemon2 = Pokemon(55,'Bullbazor',['Plant'],'Es el mejor de planta',True) 
pokemon3 = Pokemon(85,'Charmander',['Fire'],'Llamas de fuego que arden',True) 

pokemon1.display_details()
pokemon1.speak()
pokemon2.display_details()
pokemon2.speak()
pokemon3.display_details()
pokemon3.speak()
