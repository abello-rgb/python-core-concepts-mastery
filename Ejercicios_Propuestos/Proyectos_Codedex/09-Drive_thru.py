
items_list = [
    '🍔 Cheeseburger',
    '🍟 Fries',
    '🥤 Soda',
    '🍦 Ice Cream',
    '🍪 Cookie',
]



def get_item(option):
   if option > 5 or option < 0:
    print('Error: Item no disponible')
   else:  
      return items_list[option-1]



def welcome():
  option = int(input('What would you like to order? '))
  print(get_item(option))


welcome()

