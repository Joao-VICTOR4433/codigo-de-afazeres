class Atividades:
    def __init__(self,atividade):
        self.atividade=atividade
    def analise(self):
        for i in self.atividade:
            if i == "estudar pra python":
                return print("A atividade estudar python foi encontrada, no decorrer do dia foram feitas outras atividades como:",",".join(self.atividade))
        else:
            return print("Essa não foi encontrada essa atividade,mas tiveram outras que foram feitas como:",",".join(self.atividade))
 
lista=[]
afazer1=str(input("Qual sua atividade?"))
lista.append(afazer1)
while afazer1 != "parar":
    afazer1=str(input("Qual sua atividade?"))
    lista.append(afazer1)
c=Atividades(lista)
c.analise()
#","join()--> tira os couchetes ou parenteses