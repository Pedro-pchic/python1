
name ='pedro chic'
x =' '.join(name) # .join deja un espacio de la digito
print(x)

name =('pedro', 'chic')
x ='k'.join(name) # el ", " es templazado por el valor de X
print(x)

name = {'pedro':'chic','azul':'cafes'}
l = 'xxx'
x =l.join(name) #solo toma el primer valor y el 3 los une por medio de xxx valor de l 
print(x)

part1 ='United'
part2 ='States'

x =part2.join(part1)
print(x)