
# Web

#web_navigation()

def shared_printer():
  
    queue = []
    while True:


     action = input(
        'Agrega el documuento o selecciona  imprimir / salir: '
    )
     
     if action == 'salir':
       break
     elif action == 'imprimir':
       if len(queue) > 0:
         print(f'Imprimiendo {queue.pop(0)}...')
     else:
       queue.append(action)

     print(f'Cola de impresion: {queue}')


shared_printer()     
  