from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

#Extraemos del documento lifestore_file.py las listas que utilizaremos para trabajar con dichos datos posteriormente

clientes_life = [["Rosa", "123"], ["Mariana", "colegio"], ["Mario", "bros"]]
admin_life = [["Ricardo", "2020"], ["Javier", "emtech"]]
#En primer ligar definimos las variables de cleintes y administradores y asignamos el nombre y contraseña respectivamente


usuario_inicio = input("Gracias por visitar Life Store. Ingresa tu nombre: ")
usuario_contraseña = input("\nIngresa tu contraseña: ")
#Posteriormente se crean dos duevas variables para que desde un inicio al mostrar la pantalla nos pida el nombre de y la contraseña 

si_admin = 0
correcta = 0
#creamos una bandera tanto para el bloque de inicio de sesión como para el menú de administrador.

while correcta != 1:
  for usuario in clientes_life:
    if usuario[0] == usuario_inicio and usuario[1] == usuario_contraseña:
      print("\nIngresaste como cliente, no eres administrador")
      correcta = 1
      break

  for usuario in admin_life:
    if usuario[0] == usuario_inicio and usuario[1] == usuario_contraseña:
      print("\nBienvenido, has ingresado como administrador.")
      correcta = 1
      si_admin = 1
      break
#para el inicio de sesión se utilizaron dos for, el primero valida si eres cleinte de la tienda o administrador, en caso de ser cliente, mostrará el mensaje que no puede inresar como administrador, si los datos que se adjuntan son los de algún administrador, se le dará la bienvenida

if si_admin == 1:
  #si el usuario inresa como administrador se le mostrará toda la información que se encuentre en este modulo, la cual se le facilitará al administrador en opciones para una mejor visualización y acceso a la información de interés del administrador

  print("\nElige la opción del menú que quieras visualizar:\na.-Productos más vendidos.\nb.-Productos mas buscados \n")
  #A continuación se le muestra el menú al administrador de los datos de importacia que desea visualizar respecto a la información de los datos de la tienda.

  #Ahora procederemos a calcular los datos del menú respecto a las listas iniciales de Life Store, es decir, respecto de las ventas, búsquedas y productos
  
  #1.- LISTA DE PRODUCTOS ACOMODADOS [ID-DEL PRODUCTO, NOMBRE, CANTIDAD VENDIDA]
  contador= 0
  total_ventas = []

  for producto in lifestore_products:
    for ventas in lifestore_sales:
      if producto[0] == ventas[1]:
        contador += 1

    listado_nuevo_ventas = [producto[0], producto[1],contador]
    total_ventas.append(listado_nuevo_ventas)
    contador = 0
   #una vez que juntamos las dos listas tanto de ventas como de productos, tenemos ya los datos de productos que se venden con su respectivo nombre, pero en el siguiete espacio de código se hara su ordenamiento de mayor a menor

  len_total_ventas = len(total_ventas)
 
  for i in range(len_total_ventas-1):
    for j in range(len_total_ventas-i-1):
        if total_ventas[j][2]<total_ventas[j+1][2]:
          total_ventas[j],total_ventas[j+1]=total_ventas[j+1],total_ventas[j]

  #Aqui en este código ya estan acomodados los productos por ventas de mayor a menor y se mostraran con el print for que mas abajo se establece una vez que el administrado elija la opción "a"

  #2.- LISTA DE PRODUCTOS ACOMODADOS POR BUSQUEDA [ID-PRODUCTO, NOMBRE, CANTIDAD BUSQUEDA]

  total_busqueda = []

  for producto_b in lifestore_products:
    for busqueda in lifestore_searches:
      if producto_b[0] == busqueda[1]:
        contador += 1

    listado_nuevo_busqueda = [producto_b[0], producto_b[1],contador]
    total_busqueda.append(listado_nuevo_busqueda)
    contador = 0

  len_total_busqueda = len(total_busqueda)
 
 #ORDENADOS BUSQUEDAS DE MAYOR A MENOR
  for i in range(len_total_busqueda-1):
    for j in range(len_total_busqueda-i-1):
        if total_busqueda[j][2]<total_busqueda[j+1][2]:
          total_busqueda[j],total_busqueda[j+1]=total_busqueda[j+1],total_busqueda[j]

  #en este punto se le da la opcion al administrador para que ingrese la opcion que desea en el input
  opcion_seleccionada = input("Ingrese la opción que desea visualizar: ")
  
  #se establece una bandera
  si_opcion = 0

  #para que elija una opcion se va a realizar un bucle while para que elija la opcion que desea
  while si_opcion != 1:
    if opcion_seleccionada == "a":
      for total in total_ventas:
       print("El producto: ", total[1], "se vendió", total[2],"\n") 
       si_opcion = 1
    elif opcion_seleccionada == "b":
      for total_b in total_busqueda:
        print("El producto: ", total_b[1], "se buscó en linea", total_b[2], "veces""\n")
        si_opcion = 1
    else:
      print("\nLa opción que elegiste no existe, intentalo de nuevo por favor.\n")
      opcion_seleccionada = input("Ingresa otra vez la opción que deseas ver: ")
