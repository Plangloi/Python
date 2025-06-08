liste_nombres = [1, 2, 4, 23, 45, 3, 7, 11, 22]
def separer_pairs_impairs(nombres):
  
    pairs = tuple(nombre for nombre in nombres if nombre % 2 == 0)
    impairs = tuple(nombre for nombre in nombres if nombre % 2 != 0)


print("Nombres pairs :", pairs)
print("Nombres impairs :", impairs)
