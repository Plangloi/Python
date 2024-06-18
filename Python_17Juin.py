#Détermine si un nombre est premier.
def n_premier(numero):
  if numero <= 1:
    return False
  for i in range(2, numero):
    if numero % i == 0:
      return False
  return True

list_numero = [17, 33, 47, 41, 57, 67]
nombre_p = [num for num in list_numero if n_premier(num)]

print("Les nombres premiers sont :" , nombre_p)
