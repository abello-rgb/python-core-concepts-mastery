# Por valor

def change_value(value_a:int, value_b: int)-> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b
my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = change_value(my_int_d, my_int_e)
#print(f'{my_int_d}, {my_int_e}')
#print(f'{my_int_f}, {my_int_g}')

# Por referencia
def change_ref(value_a:list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b
my_list_e = [30,40]
my_list_f = [50,60]
my_list_g, my_list_h = change_ref(my_list_e, my_list_f)
print(f'{my_list_e},{my_list_f}')
print(f'{my_list_g},{my_list_h}')


