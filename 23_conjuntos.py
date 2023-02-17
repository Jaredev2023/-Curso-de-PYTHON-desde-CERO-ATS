conjunto = set()
conjunto2= set()
conjunto2={3,4,5}
conjunto={1,2,3}
a={1,2,3}
#conjunto.add(5)
#conjunto.discard(3)
#conjunto.clear()
'''print(conjunto)
print(3 in conjunto)
print(conjunto == conjunto2)
print(len(conjunto))'''
#union 
c = conjunto  | conjunto2
print(c)
#interseccion
b = conjunto  & conjunto2
#diferencia
a = conjunto  - conjunto2
#diferencia simetrica
c = conjunto  ^ conjunto2 #^= alt + 94
print(a,b,c)
print(a.issubset(c))
print(conjunto.issuperset(c))
print(conjunto.isdisjoint(conjunto2))
#conjunto=frozenset({1,2,3})