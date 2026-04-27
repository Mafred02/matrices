def mostrar_menu():
  print('''\n--- MENU DE OPERACIONES CON MATRICES ---
  1) Suma de matrices
  2) Multiplicación de matrices
  3) Producto de Hadamard
  4) Producto de Kronecker
  5) Salir''')
  while True:
    try:
      opcion = int(input("Seleccione una opción: "))
      if opcion in [1, 2, 3, 4, 5]:
        return opcion
      else:
        print("Error: opción inválida.")
    except ValueError:
      print("Error: debe ingresar un número entero.")
