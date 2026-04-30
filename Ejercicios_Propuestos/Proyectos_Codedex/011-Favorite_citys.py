
class City:
    def __init__(self,name,country,population,landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks


cienaga = City('Cienega, Magdalena', 'Colombia', 134841,'Plaza del Centenario')

orlando = City('Orlando, Florida', 'Estados Unidos',320000, 'Walt Disney World' )

print(vars(cienaga))
print(vars(orlando))