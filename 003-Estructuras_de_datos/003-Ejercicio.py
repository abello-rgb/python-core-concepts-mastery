def my_agenda():

    agenda = {
       
    }

    while True:
      
      def validar_numero(phone):
         if phone.isdigit() and len(phone) > 0 and len(phone)<= 11:
            agenda[name] = phone
         else:
          print('Debes introducir un numero de telefono con un maximo de 11 digitos.')

          
     
      
      print('1. Buscar Contacto')
      print('2. Insertar Contacto')
      print('3. Actualizar Contacto')
      print('4. Eliminar Contacto')
      print('5. Salir')
      
      option = input('Selecciona una de las opciones en pantalla :')

      match option:
        case '1':
           name = input(' Introduce el nombre del contacto a buscar')
           if name in agenda:
              print(f'El numero de telefono de {name} es {agenda[name]}')
           else:
              print(f'{name} No esta en tu agenda.')  
           pass
        case '2':
           name = input(' Introduce el nombre del contacto')
           phone = input(' Introduce el telefono del contacto')
           validar_numero(phone)
           print('Contacto Agregado exitosamente')
           pass
        case '3':
           name = input(' Introduce el nombre del contacto')
           if name in agenda:
              phone = input('Introduce el telefono del contacto')
              validar_numero(phone)
           else:
               print(f'El contacto {name} no existe.')
           pass
        case '4':
            name = input(' Introduce el nombre del contacto')
            if name in agenda:
               del agenda[name]
               print('Contacto Eliminado Exitosamente')
            else:
               print(f'El contacto {name} no existe.')
            pass
        case '5':
            print('Saliendo de la agenda')
            break
        case _:
            print('Opcion no valida. Elige una de las opciones')




my_agenda()








