def ingresar_matriz():
  while True:
    b = input("Ingrese las filas separadas por ';': ").split(";")
    A = []
    value = True
    try:
      for i in range(len(b)):
        c = b[i].split()
        if len(c) == 0:
          print("Error: debes digitar algun numero")
          value = False
          break
        else:
          a = list(map(float,c))
          A.append(a)
      if value == False:
        continue

      for j in range(len(A)):
        if len(A[j]) != len(A[0]):
          value = False
          break
      if value == True:
        return A
      else:
        print("Error: La cantidad de columnas debe ser igual para todas las filas")
    except ValueError:
      print("Error: Debes poner numeros")

def mostrar_matriz(A):
  print("Resultado:")
  for fila in A:
    print(fila)

