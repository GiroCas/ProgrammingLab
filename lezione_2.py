def sum_list( lista ):
    ris = 0
    if lista == []:
        return None
    for item in lista:
        ris = ris + item
    return ris 

my_list = []

somma = sum_list( my_list)

print ( "somma: {}".format(somma))
        
        
    