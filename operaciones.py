def suma(a, b):
  if len(a) != len(b) or len(a[0]) != len(b[0]):
    print("Error: Las matrices deben tener las mismas dimensiones para sumarse.")
  else:
    result = []
    for i in range(len(a)):
      fila = []
      for j in range(len(a[0])):
        fila.append(a[i][j] + b[i][j])
      result.append(fila)
    return result

def multiplicacion(a, b):
  if len(a[0]) != len(b):
    print("Error: la primera matriz debe tener igual cantidad de columnas que filas en la segunda matriz")
  else:
    result = []
    for i in range(len(a)):
      fila = []
      for j in range(len(b[0])):
        suma = 0
        for k in range(len(a[0])):
          suma += a[i][k] * b[k][j]
        fila.append(suma)
      result.append(fila)
    return result

def Hadamard(a, b):
  if len(a) != len(b) or len(a[0]) != len(b[0]):
    print("Error: Las matrices deben tener las mismas dimensiones")
  else:
    result = []
    for i in range(len(a)):
      fila = []
      for j in range(len(a[0])):
        fila.append(a[i][j] * b[i][j])
      result.append(fila)
    return result

def Kronecker(a, b):
  result = []
  for i in range(len(a)):
    for j in range(len(b)):
      fila = []
      for k in range(len(a[0])):
        for l in range(len(b[0])):
          fila.append(a[i][k] * b[j][l])
      result.append(fila)
  return result

