from proyecto_matrices import entrada as et
from proyecto_matrices import operaciones as op
from proyecto_matrices import menu as mn
import importlib
def iniciar():
  while True:
    opcion = mn.mostrar_menu()

    if opcion == 5:
      print("Gracias por usar el programa.")
      break
    else:
      a = et.ingresar_matriz()
      b = et.ingresar_matriz()

      if opcion == 1:
        resultado = op.suma(a, b)
      elif opcion == 2:
        resultado = op.multiplicacion(a, b)
      elif opcion == 3:
        resultado = op.Hadamard(a, b)
      elif opcion == 4:
        resultado = op.Kronecker(a, b)

      et.mostrar_matriz(resultado)
