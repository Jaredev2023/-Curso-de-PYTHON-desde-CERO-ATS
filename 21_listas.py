#listas
lista=["lunes","martes","miercoles","jueves","viernes","sabado","domingo",1,2,3,[8,9,5],True]#*2
print(lista)
print(lista[0])
#print(lista[-1])
#print(lista[0:3])
#print(lista[:3])
print(len(lista))
lista.append(6)
lista.insert(2,3)
lista.extend([6,7,8])
print(3 in lista)
print(lista.index(2))
print(lista.count(1))
lista.pop()#eliminara el ultimo elemento en la lista si no hay parametro
lista.pop(3)
lista.remove(2)
#lista.clear()
#lista.reverse()
'''lista.sort()
lista.sort(reverse=True)'''