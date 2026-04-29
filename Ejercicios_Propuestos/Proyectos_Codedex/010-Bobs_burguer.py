
class Restaurant :
  name = ''
  category = ''
  rating = 0.0
  delivery = True


bobs_burgers = Restaurant()


bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

el_sason_de_Diana = Restaurant()

el_sason_de_Diana.name = 'El Sasón de Diana'
el_sason_de_Diana.category = 'Comida costera'
el_sason_de_Diana.rating = 5.0
el_sason_de_Diana.delivery = True

pizza_factory = Restaurant()

pizza_factory.name = 'Pizza Factory'
pizza_factory.category = 'FastFood'
pizza_factory.rating = 4.5
pizza_factory.delivery = False


print(vars(bobs_burgers))
print(vars(el_sason_de_Diana))
print(vars(pizza_factory))
