name = 'pedro chic'
print(name.replace('p','y',3)) # remplaza la letra tambien dandole cual es que queremos remplazar 
#busca donde esta la letra que queremos encotrar
print(name.rfind('o'))
#nos vuelve rescribir nuestra valariable
print(name.rstrip())

print(name.split())#separa la variable por partes con []
print(name.startswith('pedro',0,10))#cuenta cuantos digitos tengo en mi varible


print(name.strip()) #me pone en miniscula mi variable
print(name.swapcase())# pone la variable todo en mayuscula
print(name.title())#las iniciales lo escribie en mayuscula 
print(name.upper())# me devuele como mayuscula todo mi variable

"""
yedro chic
4
pedro chic
['pedro', 'chic']
True
pedro chic
PEDRO CHIC
Pedro Chic
PEDRO CHIC
"""