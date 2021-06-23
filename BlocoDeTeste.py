diclista =[{'nome' : 'eduardo' , 'sexo' : 'masculino' , 'idade' : 22},{'nome' : 'eduardo' , 'sexo' : 'masculino' , 'idade' : 22}]

listasoma = []

for i in diclista:
    var = i['idade']
    listasoma.append(var)
    

soma = sum(listasoma)   
print(soma)