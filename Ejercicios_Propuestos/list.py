

market_list = ["Cebolla","Tomate","Ajo","Aceite","Papas"]



def order_list(list:list)-> list:
    list.append('Maracuya')
    order_list = sorted(list)
    return order_list







order_market_list = order_list(market_list)

print(market_list)
print(order_market_list)
